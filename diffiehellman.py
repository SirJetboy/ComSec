import random
import rabinMiller

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
else:
    print('Error')
