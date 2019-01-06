import random
import rabinMiller
import idea_display as idead

def main(choice):
		
	primeHex = "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF"
	primeNum = int(primeHex, 16)
	print("Prime number = ", primeNum)
	print("Miller–Rabin primality test : ", rabinMiller.rabinMiller(primeNum))
	generator = 2
	print("Generator = ", generator)
	print("")
	print("")



	# -------------------------------------------------------------------

	private_key_A = random.SystemRandom().getrandbits(512)
	print("Alice private key A = ", private_key_A)
	print("Computing of the number A...")
	A = pow(generator, private_key_A, primeNum)
	print("A = ", A)
	print("")
	print("")

	# -------------------------------------------------------------------

	print("Bob received the number A = ", A)
	private_key_B = random.SystemRandom().getrandbits(512)
	print("Bob private key B =", private_key_B)
	print("Computing of the number B...")
	B = pow(generator, private_key_B, primeNum)
	print("B = ", B)
	print("Computing of the shared key...")
	K_B = pow(A, private_key_B, primeNum)
	print("Bob shared key = ", K_B)
	print("")
	print("")

	# -------------------------------------------------------------------

	print("Alice received the number B = ", B)
	print("Computing of the shared key...")
	K_A = pow(B, private_key_A, primeNum)
	print("Alice shared key = ", K_A)
	print("")
	print("")

	if K_A == K_B:
		print('Success')
		print("Final shared key = ",K_A)
		file_output = open("shared_key.txt", "w")
		file_output.write(str(K_A))
		if choice == 'fc':
			print("-- Encryption --\n")
			idead.main("fc",K_A)
			return K_A
		else:
			choix = ""
			while choix not in ('O', 'N'):
				print("Voulez vous utiliser cette clé pour chiffrer un fichier ? O/N")
				choix  = input()
				if choix == "O":
					idead.main("c",K_A)
				elif choix == "N":
					break
	else:
		print('Error')


#Génère une paire de clés DH
def gen_dh_key():
	print("Taille de la clé:\n")
	print("	1- 1536 bits\n")
	print("	2- 2048 bits\n")
	print("	3- 3072 bits\n")
	print("	4- 4096 bits\n")
	while 1:
		choix = input("Choix: ")
		
		#Prime fixe provenant de la RFC.
		if choix == '1':
			primeHex = "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF"
			break
		elif choix == '2':
			primeHex = "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF"
			break
		elif choix == '3':
			primeHex = "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AAAC42DAD33170D04507A33A85521ABDF1CBA64ECFB850458DBEF0A8AEA71575D060C7DB3970F85A6E1E4C7ABF5AE8CDB0933D71E8C94E04A25619DCEE3D2261AD2EE6BF12FFA06D98A0864D87602733EC86A64521F2B18177B200CBBE117577A615D6C770988C0BAD946E208E24FA074E5AB3143DB5BFCE0FD108E4B82D120A93AD2CAFFFFFFFFFFFFFFFF"
			break
		elif choix == '4':
			primeHex = "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AAAC42DAD33170D04507A33A85521ABDF1CBA64ECFB850458DBEF0A8AEA71575D060C7DB3970F85A6E1E4C7ABF5AE8CDB0933D71E8C94E04A25619DCEE3D2261AD2EE6BF12FFA06D98A0864D87602733EC86A64521F2B18177B200CBBE117577A615D6C770988C0BAD946E208E24FA074E5AB3143DB5BFCE0FD108E4B82D120A92108011A723C12A787E6D788719A10BDBA5B2699C327186AF4E23C1A946834B6150BDA2583E9CA2AD44CE8DBBBC2DB04DE8EF92E8EFC141FBECAA6287C59474E6BC05D99B2964FA090C3A2233BA186515BE7ED1F612970CEE2D7AFB81BDD762170481CD0069127D5B05AA993B4EA988D8FDDC186FFB7DC90A6C08F4DF435C934063199FFFFFFFFFFFFFFFF"
			break
		else:
			print("Choisissez parmi les options.") 
	
	print("Génération paire de clés DH...")
	primeNum = int(primeHex, 16)
	generator = 2
	private_key_A = random.SystemRandom().getrandbits(512)
	A = pow(generator, private_key_A, primeNum)
	
	return (A, generator, primeNum), private_key_A
