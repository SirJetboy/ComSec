import idea
from pathlib import Path


def choose_key_size(choice):
    key_size = ''
    while key_size not in (96, 128, 160, 256):
        print("Please enter the key size (96, 128, 160 or 256):")
        key_size = input()
        if key_size.isdigit():
            key_size = int(key_size)
    if choice == 'c':
        print("Please enter g to generate a key or anything else if not:")
        if input() == 'g':
            key = idea.generate_random_key(key_size)
            print("key =", int(key, 2))
            return key
    key = ''
    while not key.isdigit():
        print("Please enter key:")
        key = input()
        if key.isdigit():
            key = bin(int(key))[2:][-key_size:].zfill(key_size)
    return key


def choose_file():
    path = ''
    while not Path(path).is_file():
        print("Please enter the name of the file:")
        path = "idea/" + input()
    file = open(path, "r", encoding="ISO-8859-1")
    content = file.read()
    file.close()
    return content


def cipher(key, mode):
    message = choose_file()
    path = ''
    while not path:
        print("Please enter the name of the output file:")
        path = input()
    path = "idea/" + path
    file = open(path, "w", encoding="ISO-8859-1")
    ciphered = idea.cipher(message, key, mode).replace("?", "??").replace(chr(13), "?r")
    file.write(ciphered)
    file.close()


def decipher(key, mode):
    ciphered = choose_file()
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


def main():
    choice = ''
    while choice not in ('c', 'd'):
        print("Please enter c to cipher or d to decipher:")
        choice = input()
    mode = ''
    while mode not in ('ecb', 'cbc', 'pcbc'):
        print("Please enter the block cipher mode of operation (ecb, cbc or pcbc):")
        mode = input()
    key_dec = choose_key_size(choice)
    if choice == 'c':
        cipher(key_dec, mode)
    else:
        decipher(key_dec, mode)
    print("Success")


main()
