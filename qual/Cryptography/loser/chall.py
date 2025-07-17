from Crypto.Util.number import getPrime, bytes_to_long, inverse
import random
flag = b"{REDACTED}"
m = bytes_to_long(flag)
p = getPrime(128)
q = getPrime(128)
n = p * q
phi = (p - 1) * (q - 1)
bound = int(n**0.25) // 9
d = random.randint(1, bound)
e = inverse(d, phi)

c = pow(m, e, n)
print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")

# n = 52906652894260301797515398782103835279338949628025419125264108623987826435407
# e = 49709039921642593871354200166657621523197643345169138552789856388915235753807
# c = 4465365195960524839144694281341714691914471800914125198461938678373573124624