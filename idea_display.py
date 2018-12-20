import idea

message = "That's one small step for a man, one giant leap for mankind."
key_size = 128
while key_size not in (96, 128, 160, 256):
    print("Key size: 96, 128, 160 or 256?")
    key_size = int(input())
key = idea.generate_random_key(key_size)
print("Key =", int(key, 2))
ciphered = idea.cipher(message, key)
print(ciphered)
deciphered = idea.decipher(ciphered, key)
print(deciphered)
