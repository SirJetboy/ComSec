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
				length = int(input("taille: "))
				pub_key , priv_key = cert.gen_key(length)
				break
			elif algo == "2":
				A, alpha, p = dh.gen_dh_key()
				break
	
	if choix == "2":
		pub_key_utt , priv_key_utt = cert.gen_key(2048)
	
	if choix == "3":
		dh.main("none")
	
	if choix == "4":
		idead.main("c","none","n")
	
	if choix == "5":
		while 1:
			is_dh = input("Le fichier a t-il été chiffré avec une clé DH ? O/N:")
			if is_dh == "O":
				idead.main("d","none","y")
				break
			elif is_dh == "N":
				idead.main("d","none","n")
				break
	
	if choix == "6":
		sha3.main("none","none")
	
	if choix == "7":
		key = dh.main('fc')
		print("-- Decryption --\n")
		idead.main("fd",key,"y")
	
	if choix == "8":
		break

