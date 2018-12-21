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
        print("Please enter g to generate a key:")
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

    file = open(path, "r", encoding="utf8")
    content = file.read()
    file.close()
    return content


def cipher(key):
    message = choose_file()
    path = ''
    while not path:
        print("Please enter the name of the output file:")
        path = input()
    path = "idea/" + path
    file = open(path, "w", encoding="utf8")
    ciphered = idea.cipher(message, key)
    file.write(ciphered)
    file.close()


def decipher(key):
    ciphered = choose_file()
    path = ''
    while not path:
        print("Please enter the name of the output file:")
        path = input()
    path = "idea/" + path
    file = open(path, "w", encoding="utf8")
    deciphered = idea.decipher(ciphered, key)
    file.write(deciphered)
    file.close()


def main():
    choice = ''
    while choice not in ('c', 'd'):
        print("Please enter c to cipher or d to decipher:")
        choice = input()
    key_dec = choose_key_size(choice)
    if choice == 'c':
        cipher(key_dec)
    else:
        decipher(key_dec)
    print("Success")


main()
