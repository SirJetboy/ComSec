import idea
from pathlib import Path
import sha3 

def choose_key_size(choice,key,is_from_dh):
	key_size = ''
	while key_size not in (96, 128, 160, 256):
		print("Please enter the key size (96, 128, 160 or 256):")
		key_size = input()
		if key_size.isdigit():
			key_size = int(key_size)
	
	#hash the shared_key with sha3 to get the good length
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
		else:
			key = sha3.main(key,key_size)
			return key
	else:
		print("Please enter key:")
		key = input()
		if key.isdigit():
			if is_from_dh == "n":
				key = bin(int(key))[2:][-key_size:].zfill(key_size)
			else:
				key = sha3.main(key,key_size)
			return key
	return key


def choose_file(choice):
	path = ''
	while not Path(path).is_file():
		if choice in ('c','fc'):
			print("Please enter the name of the file to encrypt:")
			path = "idea/" + input()
		elif choice == 'd':
			print("Please enter the name of the file to decrypt:")
			path = "idea/" + input()
		elif choice == 'fd':
			path = "idea/encrypted"
	file = open(path, "r", encoding="ISO-8859-1")
	content = file.read()
	file.close()
	return content


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


def main(choice,key,is_from_dh):
	if choice == "c":
		print("-- Encryption --\n")
	elif choice == "d":
		print("-- Decryption --\n")
	mode = ''
	while mode not in ('ecb', 'cbc', 'pcbc'):
		print("Please enter the block cipher mode of operation (ecb, cbc or pcbc):")
		mode = input()
	key_dec = choose_key_size(choice,key,is_from_dh)
	if choice in ('c','fc') :
		cipher(key_dec, mode, choice)
	elif choice in ('d','fd'):
		decipher(key_dec, mode, choice)
	print("Success")

#main()
