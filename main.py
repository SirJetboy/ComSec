# -*- coding: utf-8 -*-

def chiffrer_signer():
	
	



while 1:
	print('\n')
	print("****	MENU PRINCIPAL	****")
	print("Souhaitez vous:\n")
	print("	Générer une clé publique / privée (Press 1) \n")
	print("	Authentifier une clé publique / un certificat (Press 2)\n")
	print("	Partager une clé secrète (Press 3)\n")
	print("	Utiliser une clé secrète pour chiffrer un message (et le signer) (Press 4)\n")
	print("	Déchiffrer un message et vérifier la signature (Press 5)\n")
	print("	La totale : THE FULL MONTY (Press 6)\n")
	print("choix:")
	choix = input()

	if choix == "1":
		generer_cle()
	if choix == "2":
		authentifier()
	if choix == "3":
		partage()
	if choix == "4":
		chiffrer_signer()
	if choix == "5":
		dechiffrer()
	if choix == "6":
		totale()
	break
