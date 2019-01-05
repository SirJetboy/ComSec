# -*- coding: utf-8 -*-

import sha3 as sha3	
import diffiehellman as dh
import idea_display as idead


while 1:
	print('\n')
	print("****	MENU PRINCIPAL	****")
	print("Souhaitez vous:\n")
	print("	Générer une clé publique / privée (Press 1) \n")
	print("	Authentifier une clé publique / un certificat (Press 2)\n")
	print("	Partager une clé secrète (Press 3)\n")
	print("	Utiliser une clé secrète pour chiffrer un message (et le signer) (Press 4)\n")
	print("	Déchiffrer un message et vérifier la signature (Press 5)\n")
	print("	Utiliser hashage SHA3 (Press 6)\n")
	print("	La totale : THE FULL MONTY (Press 7)\n")
	print("	Quitter (Press 8)\n")
	print("choix:")
	choix = input()

	if choix == "1":
		generer_cle()
	if choix == "2":
		authentifier()
	if choix == "3":
		dh.main("none")
	if choix == "4":
		idead.main("c","none")
	if choix == "5":
		idead.main("d","none")
	if choix == "6":
		sha3.main()
	if choix == "7":
		key = dh.main('fc')
		print("-- Decryption --\n")
		idead.main("fd",key)
	if choix == "8":
		break

