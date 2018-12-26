import binascii
import numpy as np



def padding(text_to_pad,size_r):
	while len(text_to_pad) % size_r != 0:
		text_to_pad = text_to_pad + "0"
	text_pad = text_to_pad
	return text_pad

def xor(a, b):
    y = int(a, 2)^int(b,2)
    return bin(y)[2:].zfill(len(a))
	
def matrix_to_string(matrix):
	string =''
	for i in range(5):
		for j in range(5):
			string += ''.join(matrix[i][j][:])
	return string


def string_to_matrix(string):
	final_matrix = [[["0" for k in range(64)] for j in range(5)] for i in range(5)]
	offset=0
	for i in range(0, 5):
		for j in range(0, 5):
			for k in range(0, 64):
				final_matrix[i][j][k] = string[offset]
				offset = offset + 1
	return final_matrix
	
	
def parity(string):
	count_bit_1 = 0
	
	#count bit 1
	for i in range(0,len(string)): 
		if string[i] == "1":
			count_bit_1 = count_bit_1 + 1
	#set parity if counter is even or odd 
	if count_bit_1 % 2 == 0:
		parity = 0
	else:
		parity = 1
	
	return parity

def f_function(matrix):
	#etape 1: xor avec bit de parité
	
	
	
print("--- HASHAGE : SHA3 ---")

text_to_hash = "texte a hasher"
text_bin = str(bin(int(binascii.hexlify(bytes(text_to_hash, "utf8")), 16))[2:])
print("Quelle taille de hash souhaitez vous ?\n")
print("	1- 256 bits\n")
print("	2- 384 bits\n")
print("	3- 512 bits\n")

while 1:
	choix = input("Choix: ")
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
		print("Entrez une option parmi les 3.")

print ("Taille de hash choisie: ", hash_length ," bits.")


print("--Initialisation des paramètres--")

size_c = 2 * hash_length
block_size = 1600
size_r = block_size - size_c

print("taille bloc = 1600 bits, c = ", size_c , "bits, r = ", size_r,"bits") 
text_bin = padding(text_bin,size_r)
nb_iter_p = int(len(text_bin)/size_r)
nb_iter_f = 24

print("--Debut du hashage--")

#initialisation du premier bloc 5x5 de 64 bits à 0
block_0 = [[["0" for k in range(64)] for j in range(5)] for i in range(5)]
block_string = matrix_to_string(block_0)

#Debut des nb_iter
for i in range(0,nb_iter_p):
	
	ri = block_string[:size_r]
	pi = text_bin[i * size_r:(i + 1) * size_r]
	ri = xor(ri, pi)
	block_string = ri + block_string[size_r:]
	block_matrix = string_to_matrix(block_string)
	
	#Fonction f de permuation, debut des 24 iters
	for j in range(0,nb_iter_f):
		f_function(block_string)
