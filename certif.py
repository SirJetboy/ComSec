import Crypto.Util.number as CUN
import os
import random 
import sha3

#Génère paire de clés RSA, selon la taille choisie
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

	return (n, e), d


#key_to_sign = dh, (A,alpha,p)
#priv_key = rsa, d
#pub_key = rsa, (n,e)
def signer(key_to_sign,d,pub_key):
	hashed_key = sha3.main(key_to_sign,256)
	n,e = pub_key.split(':')
	signature = pow(int(hashed_key,2),int(d),int(n))
	return signature



#Certificat = pub_dh + signature
#pub_key = rsa, (n,e)
def verifier(certificat,pub_key):
	pub_dh,signature = certificat.split(':')
	hashed_key = sha3.main(pub_dh,256)
	n,e = pub_key.split(':')
	
	print("\nVérification de la signature...\n")
	decipher = pow(int(signature),int(e),int(n))
	hashed_key = int(hashed_key,2)


	if decipher == hashed_key:
		print("\nSignature vérifié, la signature provient bien de l'autorité de certification.")
	else:
		print("\nLa signature ne provient pas de l'autorité de cerification")
