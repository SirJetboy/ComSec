import random


# string message to binary message
# input: string, output: string
def message_to_bin(message):
    bin_message = ''.join([bin(ord(x))[2:].zfill(8) for x in message])
    while len(bin_message) % 64 != 0:
        bin_message = "0" + bin_message
    return bin_message


# binary message to string message
# input: list of string, output: string
def bin_to_message(bin_blocs):
    bin_message = ''.join(bin_blocs)
    bin_blocs = [bin_message[i:i + 8] for i in range(0, len(bin_message), 8)]
    return ''.join([chr(int(x, 2)) for x in bin_blocs])


# generate a random key
# input: int, output: string
def generate_random_key(key_size):
    original_key = ''
    for i in range(key_size):
        original_key = str(random.randint(0, 1)) + original_key
    return original_key


# create the encryption keys for IDEA
# input: string, output: list of string
def create_encryption_keys(original_key):
    key_bis = original_key
    key = []
    while len(key) != 52:
        while key_bis:
            key.append(key_bis[:16])
            if len(key_bis) == 16 or len(key) == 52:
                key_bis = ''
            else:
                key_bis = key_bis[16:]
        original_key = original_key[-25:] + original_key[:-25]
        key_bis = original_key
    return key


# create the decryption keys for IDEA
# input: list of string, output: list of string
def create_decryption_keys(original_key):
    key = create_encryption_keys(original_key)
    dec_key = list()
    dec_key.append((inv(key[48])))
    dec_key.append((opp(key[49])))
    dec_key.append((opp(key[50])))
    dec_key.append((inv(key[51])))
    dec_key.append((key[46]))
    dec_key.append((key[47]))
    for i in range(7):
        dec_key.append((inv(key[42 - i * 6])))
        dec_key.append((opp(key[44 - i * 6])))
        dec_key.append((opp(key[43 - i * 6])))
        dec_key.append((inv(key[45 - i * 6])))
        dec_key.append((key[40 - i * 6]))
        dec_key.append((key[41 - i * 6]))
    dec_key.append(inv(key[0]))
    dec_key.append(opp(key[1]))
    dec_key.append(opp(key[2]))
    dec_key.append(inv(key[3]))
    return dec_key


# create blocs for encryption
# input: string, output: list of string
def create_blocs(bin_message):
    bloc = []
    while len(bin_message) != 0:
        bloc.append(bin_message[:16])
        bin_message = bin_message[16:]
    return bloc


# add two numbers modulo 65536
# input: (string, string), output: string
def add(a, b):
    return bin((int(a, 2) + int(b, 2)) % 65536)[2:][-16:].zfill(16)


# multiply two numbers modulo 65537
# input: (string, string), output: string
def mul(a, b):
    if int(a, 2) == 0:
        a = '10000000000000000'
    if int(b, 2) == 0:
        a = '10000000000000000'
    return bin(int(a, 2) * int(b, 2) % 65537)[2:][-16:].zfill(16)


# xor two numbers modulo 65536
# input: (string, string), output: string
def xor(a, b):
    return bin(int(a, 2) ^ int(b, 2))[2:][-16:].zfill(16)


# compute the additive inverse modulo 65536
# input: string, output: string
def opp(a):
    return bin(- int(a,2) % 65536)[2:][-16:].zfill(16)


# compute the multiplicative inverse modulo 65537
# input: string, output: string
def inv(a):
    a = int(a, 2)
    x0, x1, y0, y1, b = 1, 0, 0, 1, 65537
    mod = b
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return bin(x0 % mod)[2:][-16:].zfill(16)


# IDEA algorithm
# input: (list of string, list of string), output: list of string
def code(bloc, key):
    temp = ['', '']
    for i in range(8):
        # 1
        bloc[0] = mul(bloc[0], key[0 + i * 6])
        # 2
        bloc[1] = add(bloc[1], key[1 + i * 6])
        # 3
        bloc[2] = add(bloc[2], key[2 + i * 6])
        # 4
        bloc[3] = mul(bloc[3], key[3 + i * 6])
        # 5
        temp[0] = xor(bloc[0], bloc[2])
        # 6
        temp[1] = xor(bloc[1], bloc[3])
        # 7
        temp[0] = mul(temp[0], key[4 + i * 6])
        # 8
        temp[1] = add(temp[1], temp[0])
        # 9
        temp[1] = mul(temp[1], key[5 + i * 6])
        # 10
        temp[0] = add(temp[0], temp[1])
        # 11
        bloc[0] = xor(bloc[0], temp[1])
        # 12
        bloc[2] = xor(bloc[2], temp[1])
        # 13
        bloc[1] = xor(bloc[1], temp[0])
        # 14
        bloc[3] = xor(bloc[3], temp[0])
        # 15
        bloc[1], bloc[2] = bloc[2], bloc[1]
    # 1
    bloc[1], bloc[2] = bloc[2], bloc[1]
    # 2
    bloc[0] = mul(bloc[0], key[48])
    # 3
    bloc[1] = add(bloc[1], key[49])
    # 4
    bloc[2] = add(bloc[2], key[50])
    # 5
    bloc[3] = mul(bloc[3], key[51])
    return bloc


# cipher function
# input: (string, string, string), output: string
def cipher(message, key, mode):
    bin_message = message_to_bin(message)
    blocs = create_blocs(bin_message)
    key_list = create_encryption_keys(key)
    ciphered_blocs = list()
    for i in range(len(blocs)//4):
        if mode == 'cbc':
            if i == 0:
                blocs[0] = xor(blocs[0], '0' * 16)
                blocs[1] = xor(blocs[1], '0' * 16)
                blocs[2] = xor(blocs[2], '0' * 16)
                blocs[3] = xor(blocs[3], '0' * 16)
            else:
                blocs[0 + i * 4] = xor(blocs[0 + i * 4], ciphered_blocs[-4])
                blocs[1 + i * 4] = xor(blocs[1 + i * 4], ciphered_blocs[-3])
                blocs[2 + i * 4] = xor(blocs[2 + i * 4], ciphered_blocs[-2])
                blocs[3 + i * 4] = xor(blocs[3 + i * 4], ciphered_blocs[-1])
        elif mode == 'pcbc':
            if i == 0:
                blocs_previous = blocs[:4]
                blocs[0] = xor(blocs[0], '0' * 16)
                blocs[1] = xor(blocs[1], '0' * 16)
                blocs[2] = xor(blocs[2], '0' * 16)
                blocs[3] = xor(blocs[3], '0' * 16)
            else:
                blocs_temp = blocs[i * 4:4 + i * 4]
                blocs[0 + i * 4] = xor(blocs[0 + i * 4], xor(blocs_previous[0], ciphered_blocs[-4]))
                blocs[1 + i * 4] = xor(blocs[1 + i * 4], xor(blocs_previous[1], ciphered_blocs[-3]))
                blocs[2 + i * 4] = xor(blocs[2 + i * 4], xor(blocs_previous[2], ciphered_blocs[-2]))
                blocs[3 + i * 4] = xor(blocs[3 + i * 4], xor(blocs_previous[3], ciphered_blocs[-1]))
                blocs_previous = blocs_temp
        ciphered_blocs.extend(code(blocs[i * 4:4 + i * 4], key_list))
    ciphered_message = bin_to_message(ciphered_blocs)
    return ciphered_message


# decipher function
# input: (string, string, string), output: string
def decipher(message, key, mode):
    bin_message = message_to_bin(message)
    blocs = create_blocs(bin_message)
    key_list = create_decryption_keys(key)
    deciphered_blocs = list()
    for i in range(len(blocs) // 4):
        deciphered_blocs.extend(code(blocs[i * 4:4 + i * 4], key_list))
        if mode == 'cbc':
            if i == 0:
                deciphered_blocs[0] = xor(deciphered_blocs[0], '0' * 16)
                deciphered_blocs[1] = xor(deciphered_blocs[1], '0' * 16)
                deciphered_blocs[2] = xor(deciphered_blocs[2], '0' * 16)
                deciphered_blocs[3] = xor(deciphered_blocs[3], '0' * 16)
            else:
                deciphered_blocs[-4] = xor(deciphered_blocs[-4], blocs[i * 4 - 4])
                deciphered_blocs[-3] = xor(deciphered_blocs[-3], blocs[i * 4 - 3])
                deciphered_blocs[-2] = xor(deciphered_blocs[-2], blocs[i * 4 - 2])
                deciphered_blocs[-1] = xor(deciphered_blocs[-1], blocs[i * 4 - 1])
        elif mode == 'pcbc':
            if i == 0:
                deciphered_blocs[0] = xor(deciphered_blocs[0], '0' * 16)
                deciphered_blocs[1] = xor(deciphered_blocs[1], '0' * 16)
                deciphered_blocs[2] = xor(deciphered_blocs[2], '0' * 16)
                deciphered_blocs[3] = xor(deciphered_blocs[3], '0' * 16)
            else:
                xor(deciphered_blocs[-8], blocs[i * 4 - 4])
                deciphered_blocs[-4] = xor(deciphered_blocs[-4], xor(deciphered_blocs[-8], blocs[i * 4 - 4]))
                deciphered_blocs[-3] = xor(deciphered_blocs[-3], xor(deciphered_blocs[-7], blocs[i * 4 - 3]))
                deciphered_blocs[-2] = xor(deciphered_blocs[-2], xor(deciphered_blocs[-6], blocs[i * 4 - 2]))
                deciphered_blocs[-1] = xor(deciphered_blocs[-1], xor(deciphered_blocs[-5], blocs[i * 4 - 1]))
    deciphered_message = bin_to_message(deciphered_blocs)
    return deciphered_message


