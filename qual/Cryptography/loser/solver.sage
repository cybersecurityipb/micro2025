#simple wiener attack aja sih
from sage.all import *

n = 52906652894260301797515398782103835279338949628025419125264108623987826435407
e = 49709039921642593871354200166657621523197643345169138552789856388915235753807
c = 4465365195960524839144694281341714691914471800914125198461938678373573124624

def wiener(n, e):
    n = Integer(n)
    e = Integer(e)
    for f in (e / n).continued_fraction().convergents()[1:]:
        k, d = f.numerator(), f.denominator()
        if d == 0 or (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k
        b = -(n - phi + 1)
        discr = b * b - 4 * n
        if discr >= 0:
            sqrt_discr = sqrt(discr)
            if sqrt_discr.is_integer():
                p = (-b + sqrt_discr) // 2
                q = (-b - sqrt_discr) // 2
                if p * q == n:
                    return (p, q, d)
    return (None, None, None)

p, q, d = wiener(n, e)

if d:
    print(f"[+] d found: {d}")
    m = power_mod(c, d, n)
    flag = bytes.fromhex(hex(m)[2:]).decode()
    print("[+] Decrypted message:", flag)

