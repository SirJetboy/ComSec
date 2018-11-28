import binascii


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


message = "question"
bin_message = str(bin(int(binascii.hexlify(bytes(message, "utf8")), 16))[2:])
# print(message)
while len(bin_message) % 64 != 0:
    bin_message = "0" + bin_message

key = ['0011111101010100', '1010010111011011', '1001000110011110', '1001001111101010',
       '1010110110101000', '0111101100101101', '0011010111100101', '0111111110000001',
       '1111001010111111', '1100000010011111']

bloc = []
while len(bin_message) != 0:
    bloc.append(bin_message[:16])
    bin_message = bin_message[16:]

print("original bin")
print(*bloc)


def add(a, b):
    return bin((int(a, 2) + int(b, 2)) % 65536)[2:][-16:].zfill(16)


def mul(a, b):
    return bin(int(a, 2) * int(b, 2) % 65537)[2:][-16:].zfill(16)


def xor(a, b):
    return bin(int(a, 2) ^ int(b, 2))[2:][-16:].zfill(16)


def code(btemp, ktemp):
    temp = ['', '']
    # 1
    btemp[0] = mul(btemp[0], ktemp[0])
    # 2
    btemp[1] = add(btemp[1], ktemp[1])
    # 3
    btemp[2] = add(btemp[2], ktemp[2])
    # 4
    btemp[3] = mul(btemp[3], ktemp[3])
    # 5
    temp[0] = xor(btemp[0], btemp[2])
    # 6
    temp[1] = xor(btemp[1], btemp[3])
    # 7
    temp[0] = mul(temp[0], ktemp[4])
    # 8
    temp[1] = add(temp[1], temp[0])
    # 9
    temp[1] = mul(temp[1], ktemp[5])
    # 10
    temp[0] = add(temp[0], temp[1])
    # 11
    btemp[0] = xor(btemp[0], temp[1])
    # 12
    btemp[2] = xor(btemp[2], temp[1])
    # 13
    btemp[1] = xor(btemp[1], temp[0])
    # 14
    btemp[3] = xor(btemp[3], temp[0])
    # 15
    btemp[1], btemp[2] = btemp[2], btemp[1]
    return btemp


# cipher
key = ['0011111101010100', '1010010111011011', '1001000110011110', '1001001111101010',
       '1010110110101000', '0111101100101101', '0011010111100101', '0111111110000001',
       '1111001010111111', '1100000010011111']

bloc = code(bloc, key)
# 1

bloc[1], bloc[2] = bloc[2], bloc[1]
# 2
bloc[0] = mul(bloc[0], key[6])
# 3
bloc[1] = add(bloc[1], key[7])
# 4
bloc[2] = add(bloc[2], key[8])
# 5
bloc[3] = mul(bloc[3], key[9])

print("ciphered bin")
print(*bloc)

# decipher
# 1
bloc[0] = mul(bloc[0], inv(key[6]))
# 2
bloc[1] = add(bloc[1], opp(key[7]))
# 3
bloc[2] = add(bloc[2], opp(key[8]))
# 4
bloc[3] = mul(bloc[3], inv(key[9]))


dkey = []

dkey.append(inv(key[6]))
dkey.append(opp(key[7]))
dkey.append(opp(key[8]))
dkey.append(inv(key[9]))
dkey.append(key[4])
dkey.append(key[5])
dkey.append(inv(key[0]))
dkey.append(opp(key[1]))
dkey.append(opp(key[2]))
dkey.append(inv(key[3]))

bloc = code(bloc, dkey)

print("deciphred bin")
print(*bloc)

print("original key")
print(*key)

print("decipher key")
print(*dkey)

# message = binascii.unhexlify('%x' % int('0b' + bloc, 2)).decode("utf-8")
# print("bin_message = " + bin_message)
# print("message = " + message)
