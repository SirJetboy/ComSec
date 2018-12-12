import binascii
import random

message = "question"
bin_message = str(bin(int(binascii.hexlify(bytes(message, "utf8")), 16))[2:])
# print(message)
while len(bin_message) % 64 != 0:
    bin_message = "0" + bin_message
original_key = ''
# for i in range(128):
#    original_key = str(random.randint(0, 1)) + original_key

original_key = "00111000111111100001011000100011101111100110111011011010110011110100010010010010011100000001000000101101111100111001100101011100"

key_bis = original_key
key = []

# add a variable to manage length keys
while len(key) != 52:
    while key_bis:
        key.append(key_bis[:16])
        if len(key_bis) == 16 or len(key) == 52:
            key_bis = ''
        else:
            key_bis = key_bis[16:]
    original_key = original_key[-25:] + original_key[:-25]
    key_bis = original_key

bloc = []
while len(bin_message) != 0:
    bloc.append(bin_message[:16])
    bin_message = bin_message[16:]
print("original")
print([int(message, 2) for message in bloc])


def add(a, b):
    return bin((int(a, 2) + int(b, 2)) % 65536)[2:][-16:].zfill(16)


def mul(a, b):
    return bin(int(a, 2) * int(b, 2) % 65537)[2:][-16:].zfill(16)


def xor(a, b):
    return bin(int(a, 2) ^ int(b, 2))[2:][-16:].zfill(16)


def opp(a):
    return bin(- int(a,2) % 65536)[2:][-16:].zfill(16)


def inv(a):
    a = int(a, 2)
    x0, x1, y0, y1, b = 1, 0, 0, 1, 65537
    mod = b
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return bin(x0 % mod)[2:][-16:].zfill(16)


def code(bloc_temp, key_temp):
    temp = ['', '', '', '', '', '']
    for i in range(8):
        # 1
        bloc_temp[0] = mul(bloc_temp[0], key_temp[0 + i * 6])
        # 2
        bloc_temp[1] = add(bloc_temp[1], key_temp[1 + i * 6])
        # 3
        bloc_temp[2] = add(bloc_temp[2], key_temp[2 + i * 6])
        # 4
        bloc_temp[3] = mul(bloc_temp[3], key_temp[3 + i * 6])
        # 5
        temp[0] = xor(bloc_temp[0], bloc_temp[2])
        # 6
        temp[1] = xor(bloc_temp[1], bloc_temp[3])
        # 7
        temp[2] = mul(temp[0], key_temp[4 + i * 6])
        # 8
        temp[3] = add(temp[1], temp[2])
        # 9
        temp[5] = mul(temp[3], key_temp[5 + i * 6])
        # 10
        temp[4] = add(temp[2], temp[5])
        # 11
        bloc_temp[0] = xor(bloc_temp[0], temp[5])
        # 12
        bloc_temp[2] = xor(bloc_temp[2], temp[5])
        # 13
        bloc_temp[1] = xor(bloc_temp[1], temp[4])
        # 14
        bloc_temp[3] = xor(bloc_temp[3], temp[4])
        # 15
        bloc_temp[1], bloc_temp[2] = bloc_temp[2], bloc_temp[1]
    return bloc_temp


# cipher
bloc = code(bloc, key)
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

print("ciphered")
print([int(message, 2) for message in bloc])


# decipher
dec_key = []
for i in range(8):
    dec_key.append((inv(key[48 - i * 6])))
    dec_key.append((opp(key[49 - i * 6])))
    dec_key.append((opp(key[50 - i * 6])))
    dec_key.append((inv(key[51 - i * 6])))
    dec_key.append((key[46 - i * 6]))
    dec_key.append((key[47 - i * 6]))
dec_key.append(inv(key[0]))
dec_key.append(opp(key[1]))
dec_key.append(opp(key[2]))
dec_key.append(inv(key[3]))

# 1
bloc[0] = mul(bloc[0], dec_key[0])
# 2
bloc[1] = add(bloc[1], dec_key[1])
# 3
bloc[2] = add(bloc[2], dec_key[2])
# 4
bloc[3] = mul(bloc[3], dec_key[3])

bloc = code(bloc, dec_key)

print("deciphred")
print([int(subkey, 2) for subkey in bloc])
#message = binascii.unhexlify('%x' % int('0b' + bin_message, 2)).decode("utf-8")
#print("message = " + message)
