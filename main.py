# -*- coding: utf-8 -*-

import sha3 as sha3	
import diffiehellman as dh
import idea_display as idead
import os
import certif as cert


while 1:

	print('\n')
	print("****	MENU PRINCIPAL	****")
	print("Souhaitez vous:\n")
	print("	1- Générer une paire de clé publique / privée\n")
	print("	2- Authentifier une clé publique / un certificat\n")
	print("	3- Générer une clé secrète partagée\n")
	print("	4- Utiliser une clé secrète pour chiffrer un message (et le signer) \n")
	print("	5- Déchiffrer un message et vérifier la signature\n")
	print("	6- Utiliser hashage SHA3\n")
	print("	7- La totale : THE FULL MONTY\n")
	print("	8- Quitter\n")
	choix = input("choix:")

	if choix == "1":
		while 1:
			print("1- Générer clés RSA\n")
			print("2- Générer clés DiffieHellman\n")
			algo = input("choix:")	
			
			if algo == "1":
				pub_key , priv_key = cert.gen_key()
				print("Public key = ",pub_key)
				print("Private key = ",priv_key)
				break
			elif algo == "2":
				pub_key , priv_key = dh.gen_dh_key()
				print("Public key = ",pub_key)
				print("Private key = ",priv_key)
				break
	if choix == "2":
		pub_key_utt , priv_key_utt = cert.gen_key(2048)
	
	if choix == "3":
		dh.main("none")
	
	if choix == "4":
		idead.main("c","none")
	
	if choix == "5":
		idead.main("d","none")
	
	if choix == "6":
		sha3.main("none","none")
	
	if choix == "7":
		key = dh.main('fc')
		print("-- Decryption --\n")
		idead.main("fd",key)
	
	if choix == "8":
		break

