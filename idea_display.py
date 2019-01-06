import idea
from pathlib import Path
import sha3 


# to choose the key size if necessary
# input: (string, string), output: string
def choose_key_size(choice, key):
	key_size = ''
	while key_size not in (96, 128, 160, 256):
		print("Please enter the key size (96, 128, 160 or 256):")
		key_size = input()
		if key_size.isdigit():
			key_size = int(key_size)
	
	if choice == 'fd' or choice == 'fc':
		key = sha3.main(key,key_size)
		return key
	
	if choice == 'c':
		if key == "none":
			print("Please enter g to generate a key or anything else if not:")
			if input() == 'g':
				key = idea.generate_random_key(key_size)
				print("key =", int(key, 2))
				return key
			else:
				print("Please enter key:")
				key = input()
				if key.isdigit():
					key = bin(int(key))[2:][-key_size:].zfill(key_size)
					return key
		else:
			key = sha3.main(key,key_size)
			return key
	else:
		while 1:
			is_from_dh = input("Le fichier a t-il été chiffré avec une clé DH provenant de l'option 3 ? O/N:")
			if is_from_dh == "N":
				print("Please enter key:")
				key = input()
				if key.isdigit():
					key = bin(int(key))[2:][-key_size:].zfill(key_size)
					return key
			elif is_from_dh == "O":
				print("Please enter key:")
				key = input()
				if key.isdigit():
					key = sha3.main(key,key_size)
					return key


# to choose and read the content of a file
# input: string, output: string
def choose_file(choice):
	path = ''
	while not Path(path).is_file():
		if choice in ('c','fc'):
			print("\nPlease enter the name of the file to encrypt:")
			path = "idea/" + input()
		elif choice == 'd':
			print("\nPlease enter the name of the file to decrypt:")
			path = "idea/" + input()
		elif choice == 'fd':
			path = "idea/encrypted"
	file = open(path, "r", encoding="ISO-8859-1")
	content = file.read()
	file.close()
	return content


# cipher function
# input: (string, string, string)
def cipher(key, mode, choice):
	message = choose_file(choice)
	path = ''
	while not path:
		if choice == 'c':
			print("Please enter the name of the output file:")
			path = input()
		else:
			path = "encrypted"
	path = "idea/" + path
	file = open(path, "w", encoding="ISO-8859-1")
	ciphered = idea.cipher(message, key, mode).replace("?", "??").replace(chr(13), "?r")
	file.write(ciphered)
	file.close()


# decipher function
# input: (string, string, string)
def decipher(key, mode, choice):
    ciphered = choose_file(choice)
    i = 0
    while i != len(ciphered):
        if ciphered[i] == "?":
            if ciphered[i + 1] == "r":
                ciphered = ciphered[:i] + chr(13) + ciphered[i + 2:]
            else:
                ciphered = ciphered[:i + 1] + ciphered[i + 2:]
        i += 1
    path = ''
    while not path:
        print("Please enter the name of the output file:")
        path = input()
    path = "idea/" + path
    file = open(path, "w", encoding="ISO-8859-1")
    deciphered = idea.decipher(ciphered, key, mode)
    file.write(deciphered)
    file.close()


# main display
# input: (string, string)
def main(choice,key):
	if choice == "c":
		print("-- Encryption --\n")
	elif choice == "d":
		print("-- Decryption --\n")
	mode = ''
	while mode not in ('ecb', 'cbc', 'pcbc'):
		print("Please enter the block cipher mode of operation (ecb, cbc or pcbc):")
		mode = input()
	key_dec = choose_key_size(choice,key)
	if choice in ('c','fc') :
		cipher(key_dec, mode, choice)
	elif choice in ('d','fd'):
		decipher(key_dec, mode, choice)
	print("Success")
