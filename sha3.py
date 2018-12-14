import binascii
import numpy as np



def padding(text_to_pad,size_r):
	while len(text_to_pad) % size_r != 0:
		text_to_pad = "0" + text_to_pad
	text_pad = text_to_pad
	return text_pad

def xor(a, b):
    return bin(int(a, 2) ^ int(b, 2))[2:][-16:].zfill(16)

def array_to_string(block_hashing):
	block_string =''
	for i in range(5):
		for j in range(5):
			block_string += ''.join(block_hashing[i][j][:])
	return block_string



print("---HASHAGE : SHA3---")

text_to_hash = "texte a hasher"
text_bin = str(bin(int(binascii.hexlify(bytes(text_to_hash, "utf8")), 16))[2:])
print(text_bin)
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
		print("Entrez un chiffre entre 1 et 3 svp.")

print ("Taille de hash choisie: ", hash_length ," bits.")


print("--Initialisation des paramètres--")

size_c = 2 * hash_length
block_size = 1600
size_r = block_size - size_c
nb_iter=24

print("taille bloc = 1600 bits, c = ", size_c , "bits, r = ", size_r,"bits") 
text_bin = padding(text_bin,size_r)

print("--Debut du hashage--")

#initialisation du premier bloc 5x5 de 64 bits à 0
block_0 = [[["0" for k in range(64)] for j in range(5)] for i in range(5)]
block_0_string = array_to_string(block_0)

#Debut des nb_iter=24 iterations
for i in range(0,nb_iter):
	r = block_0_string[:size_r]
	print("text_bin",text_bin)
	string_p = text_bin[i * size_r:(i + 1) * size_r]
	print("r ",r)
	print("string_p", string_p)
	
	#next_r = xor(r, string_p)
	
