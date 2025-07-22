from ecc import *
from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import random
import hashlib
import json


with open("flag.txt") as f:
    flag = f.read().strip().encode()

curve = EllipticCurve()
ecdsa_system = ECDSA(curve)
d = ecdsa_system.private_key
public_key = ecdsa_system.public_key

class Farmer:
    def __init__(self):
        self.ubi_harvested = 0
        self.signatures = []

class UbiFarm:
    def __init__(self):
        self.total_ubi = 5

        self.m =  getPrime(64)
        self.a = random.randrange(1, self.m)
        self.c = random.randrange(1, self.m)
        self.seed = random.randrange(1, self.m)

    def get_keystream(self, length):
        states_needed = (length + 7) // 8 
        ks = bytearray()
        for _ in range(states_needed):
            self.seed = (self.a * self.seed + self.c) % self.m
            ks += self.seed.to_bytes(8, 'big')
        return bytes(ks[:length])

    def encrypt_ubi(self, ubi_json):
        raw = ubi_json.encode()
        raw = raw.ljust(32, b'\x00')
        ks = self.get_keystream(len(raw))
        ct = bytes(p ^ k for p, k in zip(raw, ks))
        return ct.hex()

    def validate_cleaned_ubi(self, user_input_hex, expected_json):
        try:
            ct = bytes.fromhex(user_input_hex)
            ks = self.get_keystream(len(ct))
            pt = bytes(c ^ k for c, k in zip(ct, ks))
            pt = pt.rstrip(b'\x00')
            return json.loads(pt.decode()) == json.loads(expected_json)
        except:
            return False

print(r"""
Welcome to 
 _____                                   _____                                          _      _ 
/__   \  __ _  _ __    __ _  _ __ ___   /__   \  __ _  _ __    __ _  _ __ ___    /\ /\ | |__  (_)
  / /\/ / _` || '_ \  / _` || '_ ` _ \    / /\/ / _` || '_ \  / _` || '_ ` _ \  / / \ \| '_ \ | |
 / /   | (_| || | | || (_| || | | | | |  / /   | (_| || | | || (_| || | | | | | \ \_/ /| |_) || |
 \/     \__,_||_| |_| \__,_||_| |_| |_|  \/     \__,_||_| |_| \__,_||_| |_| |_|  \___/ |_.__/ |_|

""")

farmer = Farmer()
farm = UbiFarm()

print("Selamat datang, Petani Magang!!!")
print("Tugasmu adalah memanen ubi jalar di ladang ini.")
print("Setiap ubi yang kamu panen dengan tepat akan kami berikan upah yang layak.")
print("Saat ini, ada tepat 5 ubi yang sudah layak untuk dipanen.")
print("Nah, selamat bekerja dan tunjukkan jati dirimu sebagai petani sejati!")
print(f"Eh, apa ini {public_key}")
print(f"WAIITTTT, Bapak Agoyy, pemilik ladang yang baik hati dan bijaksana ingin memberikan sedikit nasihat: {base64.b64encode(long_to_bytes(ecdsa_system.leak_generator())).decode()}")
print("Jangan lupa, kamu harus membersihkan ubi sebelum mendapatkan tanda tangan dari Bapak Agoyy.")
print("Biar bapak kasih contoh cara panen dan membersihkan ubi:")
ubi_no = str(farmer.ubi_harvested)
ubi_berat = random.randint(1, 9)
ubi = json.dumps({"ubi_no": ubi_no, "ubi_berat": ubi_berat})
encrypted_ubi = farm.encrypt_ubi(ubi)
print(f"Ini ubi kotornya : {encrypted_ubi}")
print(f"Nah, ini ubi yang bersihnya : {ubi}")

while True:
    print("\n-------------Menu Petani Magang-------------")
    print(f"Ubi dipanen: {farmer.ubi_harvested}")
    print("1. Panen Ubi")
    print("2. Jual Hasil Panen")
    print("3. Keluar")

    try:
        choice = int(input("> "))
    except ValueError:
        print("Pilihan tidak valid. Silakan coba lagi.")
        continue

    if choice == 1:
        if farmer.ubi_harvested >= farm.total_ubi:
            print("Tidak ada ubi lagi yang bisa dipanen.")
            continue

        ubi_no = str(farmer.ubi_harvested)
        ubi_berat = random.randint(1, 9)
        ubi = json.dumps({"ubi_no": ubi_no, "ubi_berat": ubi_berat})
        encrypted_ubi = farm.encrypt_ubi(ubi)

        print(f"Bapak Agoyy mengacak data ubi: {encrypted_ubi}")
        print("Coba bersihkan ubi dan kembalikan dalam bentuk hex!")

        user_input = input("(hex) > ").strip()
        if farm.validate_cleaned_ubi(user_input, ubi):
            print("Ubi berhasil dibersihkan! Kamu dapat tanda tangan.")
            message = f"ubi#{ubi_no}".encode()
            r, s = ecdsa_system.sign(message)
            farmer.signatures.append((r, s, message))
            farmer.ubi_harvested += 1
            print(f"Tanda tangan untuk {message.decode()}:")
            print(f"r = {r}")
            print(f"s = {s}")
        else:
            print("Ubi masih kotor... Coba lagi.")

    elif choice == 2:
        if farmer.ubi_harvested < farm.total_ubi:
            print("Belum cukup hasil panen! Kumpulkan semua dulu (5 ubi)!")
        else:
            key = hashlib.sha256(long_to_bytes(d)).digest()
            iv = os.urandom(16)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            encrypted_flag = iv + cipher.encrypt(pad(flag, 16))
            print("Selamat! Kamu resmi jadi pewaris ladang!")
            print("Berikut hadiahmu yang terkunci oleh kunci petani sejati:")
            print(encrypted_flag.hex())
            break

    elif choice == 3:
        print("Sampai jumpa, Petani Magang!")
        break

    else:
        print("Pilihan tidak dikenal.")
