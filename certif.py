import Crypto.Util.number as CUN
import os
import random 

#Generate RSA pub and priv key
def gen_key(key_size):
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

	return (n,e), (p, q, d)


#def signer():
