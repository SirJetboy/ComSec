import binascii
import lfsr as lfsr
import numpy as np
from math import *
from pathlib import Path



#Padding function
def padding(text_to_pad,size_r):
	while len(text_to_pad) % size_r != 0:
		text_to_pad = text_to_pad + "0"
	text_pad = text_to_pad
	return text_pad

#Binary XOR
def xor(a, b):
	y = int(a, 2)^int(b,2)
	return bin(y)[2:].zfill(len(a))

#Binary AND
def bin_and(a, b):
	y = a & b
	return bin(y)[2:]
	
#Function to get a string from a matrix
def matrix_to_string(matrix):
	string =''
	for i in range(5):
		for j in range(5):
			string += ''.join(matrix[i][j][:])
	return string

#Function to get a matrix from a string
def string_to_matrix(string):
	final_matrix = [[["0" for k in range(64)] for j in range(5)] for i in range(5)]
	offset=0
	for i in range(0, 5):
		for j in range(0, 5):
			for k in range(0, 64):
				final_matrix[i][j][k] = string[offset]
				offset = offset + 1
	return final_matrix
	

#Function to compute parity bit of a binary word
def parity(string):
	count_bit_1 = 0
	
	#count bit 1
	for i in range(0,len(string)): 
		if string[i] == "1":
			count_bit_1 = count_bit_1 + 1
			
	#set parity if counter is even or odd 
	if count_bit_1 % 2 == 0:
		parity = "0"
	else:
		parity = "1"
	
	return parity



#F function 
def f_function(matrix):
	
	#etape 1: xor avec bit de parité
	#B[:, j, k] ← B[:, j, k] ⊕ parite(B[:, j, k − 1])
	"""
	for i in range(0,5):
		for j in range(0,5):
			for k in range(0,64):
				matrix[:][j][k] = str(xor(''.join(matrix[:][j][k]), parity(''.join(matrix[:][j][k-1]))))
	"""	

	#etape 2: Permutation des mots de 64 bits, de t bits. t definit selon notre choix, par les indices (i,j).
	for i in range(0,5):
		for j in range(0,5):
			word=''.join(matrix[i][j])
			word = int(word,2)
			t = (5 * i + 2 * j + 5)%64
			shifted_word = ((word>>t)|(word<<(64-t)))&((1<<64)-1)
			shifted_word = bin(shifted_word)[2:].zfill(64)
			matrix[i][j] = list(shifted_word)
		
	
	#etape 3: Permutation B[i, j, :] ← B[j, 2i+3j, :] avec  2i+3j mod 5
	for i in range(0,5):
		for j in range(0,5):
			permut = (2 *i + 3 * j) % 5	
			matrix[i][j] = matrix[j][permut]
	
	#etape 4: Xor entre lignes. B[:, j, :] ← B[:, j, :] ⊕ (B[:, j + 1, :]&B[:, j − 1, :])
	for i in range(0,5):
		for j in range(0,5):
			word_1 = ''.join(matrix[i][(j+1)%5])
			word_2 = ''.join(matrix[i][(j-1)%5])
			word_1 = int(word_1,2)
			word_2 = int(word_2,2)
			res_and = bin_and(word_1, word_2).zfill(64)
			res_xor = xor(''.join(matrix[i][j]), res_and)
			matrix[i][j] = list(res_xor)
	
	#etape 5: Xor entre bit des mots de 64bits. B[j, j, :] ← B[j, j, 2 m − 1] ⊕ B[j, j, m + 7 × L(m)]
	for j in range(0,5):
		for m in range(0,7):
			x = (2**m - 1 ) % 64
			y = ( m + 7 * L.next() ) % 64
			res_xor = xor(matrix[j][j][x], matrix[j][j][y])
			matrix[j][j][m] = res_xor
	
	return matrix



print("--- SHA3 ---")

text_to_hash =""
print("Choose an option:\n")
print("	1- Hash the content of a file\n")
print("	2- Hash input text\n")

while 1:
	choix = input("choice: ")
	if choix == '1':
		path=''
		while not Path(path).is_file():
			path = input("file path: ")
		f = open(path, "r",encoding="ISO-8859-1")
		text_to_hash = f.read() 
		break
	elif choix == '2':
		text_to_hash = input("text to hash: ")
		break
	else:
		print("Choose between both of the options, please.")


text_bin = str(bin(int(binascii.hexlify(bytes(text_to_hash, "utf8")), 16))[2:])
print("Choose a hash length:\n")
print("	1- 256 bits\n")
print("	2- 384 bits\n")
print("	3- 512 bits\n")

while 1:
	choix = input("choice: ")
	if choix == '1':
		hash_length = 256
		break
	elif choix == '2':
		hash_length = 384
		break
	elif choix == '3':
		hash_length = 512
		break
	else:
		print("Choose between the three options, please.")

print ("Hash length: ", hash_length ," bits.")


print("\n--Parameters initialization--")

#LFSR de 8 bits
state = np.array([1, 0, 1, 0, 1, 0, 1, 0])
L = lfsr.LFSR(fpoly=[8, 6, 4, 3, 2], initstate=state)

size_c = 2 * hash_length
block_size = 1600
size_r = block_size - size_c

print("taille bloc = 1600 bits, c = ", size_c , "bits, r = ", size_r,"bits") 
text_bin = padding(text_bin,size_r)
nb_iter_p = int(len(text_bin)/size_r)
nb_iter_f = 24

print("\n-- Start of the Hashing algorithm --")
print("Computing...")

#initialisation du premier bloc 5x5 de 64 bits à 0
block_0 = [[["0" for k in range(64)] for j in range(5)] for i in range(5)]
block_string = matrix_to_string(block_0)

#ABSORPTION. 
for i in range(0,nb_iter_p):
	
	ri = block_string[:size_r]
	pi = text_bin[i * size_r:(i + 1) * size_r]
	ri = xor(ri, pi)
	block_string = ri + block_string[size_r:]
	block_matrix = string_to_matrix(block_string)
	
	#Fonction f de permuation, debut des 24 iters.
	for j in range(nb_iter_f):
		block_matrix = f_function(block_matrix)

block_string = matrix_to_string(block_matrix)


#RECUPERATION
#hash d'une taille hash_length bits. Fonction f appliqué m-1 avec m=p/r arrondie excès.
m = ceil(hash_length/size_r)
nb_iter_recup = m - 1

final_hash=""

if nb_iter_recup != 0:
	for i in range(nb_iter_recup):
		final_hash = final_hash + block_string[:size_r]
		block_matrix = string_to_matrix(block_string)
		block_matrix = f_function(block_matrix)
		block_string = matrix_to_string(block_matrix)
else:
	final_hash = block_string[:size_r]

print("\n-- Ending --")

final_hash_bin = final_hash[:hash_length]
final_hash_hex = hex(int(final_hash_bin, 2))

print("Binary final hash: ",final_hash_bin)
print("Hexa final hash: ",final_hash_hex)


file_output = open("output_hash.txt", "w")
file_output.write(final_hash_bin)
file_output.write("\n")
file_output.write(final_hash_hex)
file_output.close()
print("hashes have been saved in output_hash.txt")
