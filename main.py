# -*- coding: utf-8 -*-

import sha3 as sha3	
import diffiehellman as dh
import idea_display as idead
import os
import certif as cert
from pathlib import Path


#Menu principal du programme
while 1:

	print('\n')
	print("****	MENU PRINCIPAL	****")
	print("Souhaitez vous:\n")
	print("	1- Générer une paire de clé publique / privée\n")
	print("	2- Authentifier une clé publique / un certificat\n")
	print("	3- Générer une clé secrète partagée\n")
	print("	4- Utiliser une clé secrète pour chiffrer un message \n")
	print("	5- Déchiffrer un message\n")
	print("	6- Utiliser hashage SHA3\n")
	print("	7- La totale : THE FULL MONTY\n")
	print("	8- Quitter\n")
	choix = input("choix:")

	
	if choix == "1":
		while 1:
			print("1- Générer clés RSA\n")
			print("2- Générer clés DiffieHellman\n")
			print("3- Retour\n")
			algo = input("choix:")	
			
			#Génère clés RSA
			if algo == "1":
				pub_key , priv_key = cert.gen_key()
				print("Public key = ",pub_key)
				print("Private key = ",priv_key)
				break
			#Génère clés DH	
			elif algo == "2":
				pub_key , priv_key = dh.gen_dh_key()
				print("Public key = ",pub_key)
				print("Private key = ",priv_key)
				file_output = open("key_cert/pub_dh_key.txt", "w")
				file_output.write(str(pub_key[0]))
				file_output.write(str(pub_key[1]))
				file_output.write(str(pub_key[2]))
				file_output.close()
				print("\nLa clé publique a été sauvegardé dans key_cert/pub_dh_key.txt")
				break
			elif algo == "3":
				break
	
	if choix == "2":
		while 1:
			print("1- Générer clés de l'autorité\n")
			print("2- Signer clé\n")
			print("3- Vérifier signature\n")
			print("4- Retour\n")
			choix2 = input("choix:")	
			
			#Génère clés de l'autorité et les stocke
			if choix2 == "1":
				pub_key_utt , priv_key_utt = cert.gen_key()
				file_output = open("key_cert/utt_priv_key.txt", "w")
				file_output.write(str(priv_key_utt))
				file_output.close()
				file_output = open("key_cert/utt_pub_key.txt", "w")
				file_output.write(str(pub_key_utt[0]))
				file_output.write(":")
				file_output.write(str(pub_key_utt[1]))
				file_output.close()
				print("Paire de clés stockée")
				break
				
			#Signe une clé publique DH via le tier de confiance.
			elif choix2 == "2":
				file_key=''
				while not Path(file_key).is_file():
					file_key = input("fichier contenant clé DH à signer:")	
					file_key = "key_cert/" + file_key
				file = open(file_key, "r")
				dh_key = file.read()
				file.close()
				file = open("key_cert/utt_priv_key.txt", "r")
				priv_utt = file.read()
				file.close()
				file = open("key_cert/utt_pub_key.txt", "r")
				pub_utt = file.read()
				file.close()
				signature = cert.signer(dh_key,priv_utt,pub_utt)
				print("\nSignature de la clé = ",signature)
				certif = open("key_cert/cert_user.txt", "w")
				certif.write(str(dh_key))
				certif.write(":")
				certif.write(str(signature))
				certif.close()
				print("\nCertificat stocké dans key_cert/cert_user.txt")
				break
				
			#Vérifier signature avec clé publique de l'autorité
			elif choix2 == "3":
				file_cert=''
				while not Path(file_cert).is_file():
					file_cert = input("fichier contenant le certificat à vérifier:")
					file_cert = "key_cert/" + file_cert	
				file = open(file_cert, "r")
				certif = file.read()
				file.close()
				print("\nRécupération de la clé publique de l'autorité...\n")
				file = open("key_cert/utt_pub_key.txt", "r")
				pub_utt = file.read()
				file.close()
				cert.verifier(certif,pub_utt)
				break
			elif choix2 == "4":
				break
				
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

