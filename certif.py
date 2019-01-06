import Crypto.Util.number as CUN
import os
import random 

#Generate RSA pub and priv key
def gen_key():
	print("Taille de la clé:\n")
	print("	1- 1024 bits\n")
	print("	2- 2048 bits\n")
	print("	3- 4096 bits\n")
	while 1:
		choix = input("Choix: ")
		if choix == '1':
			key_size = 1024
			break
		elif choix == '2':
			key_size = 2048
			break
		elif choix == '3':
			key_size = 4096
			break
		else:
			print("Choisissez parmi les options.") 
	print("Génération paire de clés...")
	p = CUN.getPrime(key_size)
	q = CUN.getPrime(key_size)
	n = p * q
	phi = (p-1)*(q-1)
	
	while True:
		e = random.SystemRandom().randint(0, phi)
		if CUN.GCD(e,phi) == 1:
			break
	
	#private key
	d = CUN.inverse(e,phi)

	return (hex(n),hex(e)), (hex(p), hex(q), hex(d))


#def signer():
