#!/usr/bin/env python3
import random
from Crypto.Util.number import bytes_to_long
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
import hashlib
import os

class EllipticCurve:
    def __init__(self):
        self.p = 39402006196394479212279040100143613805079739270465446667948293404245721771496870329047266088258938001861606973112319
        self.a = -3
        self.b = 0xB3312FA7E23EE7E4988E056BE3F82D19181D9C6EFE8141120314088F5013875AC656398D8A2ED19D2A85C8EDD3EC2AEF
        self.Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        self.Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
        self.generator = (self.Gx, self.Gy)
        self.n = 39402006196394479212279040100143613805079739270465446667946905279627659399113263569398956308152294913554433653942643
    
    @staticmethod
    def inverse(n, modulus):
        return pow(n, -1, modulus)
    
    def point_add(self, P, Q):
        """Add two points on the elliptic curve"""
        if P == (None, None): 
            return Q
        if Q == (None, None): 
            return P
        (x1, y1), (x2, y2) = P, Q
        if x1 == x2 and (y1 + y2) % self.p == 0: return (None, None)
        if P == Q:
            l = (3 * x1 * x1 + self.a) * self.inverse(2 * y1, self.p) % self.p
        else:
            l = (y2 - y1) * self.inverse(x2 - x1, self.p) % self.p
        x3 = (l * l - x1 - x2) % self.p
        y3 = (l * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def scalar_mult(self, k, P):
        R = (None, None)
        if k == 0:
            return (None, None)
        if k < 0:
            k = -k
            P = (P[0], -P[1] % self.p)
        while k:
            if k & 1: R = self.point_add(R, P)
            P = self.point_add(P, P)
            k >>= 1
        return R

class ECDSA:
    def __init__(self, curve):
        self.curve = curve
        self.private_key = random.randint(1, self.curve.n - 1)
        self.public_key = self.curve.scalar_mult(self.private_key, self.curve.generator)
        self.bound = random.choice([2**19, 2**41, 2**83])
        self.a = random.randrange(1, self.bound << 7)
        self.b = random.randrange(1, self.bound)
        self.c = random.randrange(1, self.bound >> 7)
        self.last_k = random.randrange(1, self.curve.n)

    def generate_nonce(self):
        current_k = self.last_k
        next_k = (self.a * current_k**2 + self.b * current_k + self.c) % self.curve.n
        self.last_k = next_k
        return current_k
    
    def leak_generator(self):
        greyy = lambda x: (2*x) ^ x ^ (x//2) ^ (x//4)
        leak = self.bound
        for _ in range(200): leak = greyy(leak)
        return leak
    
    def sign(self, message):
        h = bytes_to_long(hashlib.sha512(message).digest())
        k = self.generate_nonce()
        P = self.curve.scalar_mult(k, self.curve.generator)
        r = P[0] % self.curve.n
        k_inv = self.curve.inverse(k, self.curve.n)
        s = (k_inv * (h + self.private_key * r)) % self.curve.n
        return (r, s)

    def verify(self, message, signature):
        r, s = signature
        if not (1 <= r < self.curve.n) or not (1 <= s < self.curve.n):
            return False
        h = bytes_to_long(hashlib.sha512(message).digest())
        w = self.curve.inverse(s, self.curve.n)
        u1 = (h * w) % self.curve.n
        u2 = (r * w) % self.curve.n
        p1 = self.curve.scalar_mult(u1, self.curve.generator)
        p2 = self.curve.scalar_mult(u2, self.public_key)
        point = self.curve.point_add(p1, p2)
        return point[0] % self.curve.n == r
    
    
