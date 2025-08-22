#!/usr/bin/env python3

from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from os import urandom
from random import SystemRandom
import json

FLAG = 'ITFEST25{dpr_kocak_joget_doang_kagak_kerja_apa_apa_mending_gw_jadi_dpr}'
rng = SystemRandom()

class Challenge:
    def __init__(self):
        self.message = urandom(16).hex()
        self.key = urandom(16)
        self.query_count = 0
        self.max_queries = 12_000

    def update_query_count(self):
        self.query_count += 1
        if self.query_count >= self.max_queries:
            self.exit = True

    def get_ct(self):
        iv = urandom(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        ct = cipher.encrypt(self.message.encode("ascii"))
        return {"ct": (iv+ct).hex()}

    def check_padding(self, ct):
        ct = bytes.fromhex(ct)
        iv, ct = ct[:16], ct[16:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        pt = cipher.decrypt(ct)  # does not remove padding
        try:
            unpad(pt, 16)
        except ValueError:
            good = False
        else:
            good = True
        self.update_query_count()
        return {"result": good ^ (rng.random() > 0.25)}

    def check_message(self, message):
        if message != self.message:
            self.exit = True
            return {"error": "incorrect message"}
        return {"flag": FLAG}

    def challenge(self, msg):
        if "option" not in msg or msg["option"] not in ("encrypt", "unpad", "check"):
            return {"error": "Option must be one of: encrypt, unpad, check"}

        if msg["option"] == "encrypt": return self.get_ct()
        elif msg["option"] == "unpad": return self.check_padding(msg["ct"])
        elif msg["option"] == "check": return self.check_message(msg["message"])

def main():
    chall = Challenge()
    print("This is a padding oracle challenge, ahh ummmm, I mean, a CBC oracle challenge, maybe with noise?")
    print("Send your input as JSON.")
    print('Example: {"option": "encrypt"}')

    while True:
        try:
            user_input = input("> ")
            if not user_input:
                continue
            json_input = json.loads(user_input)
            response = chall.challenge(json_input)
            chall.query_count += 1
            print(json.dumps(response))
            print(chall.query_count, "queries made so far.")
            if chall.query_count >= chall.max_queries:
                print("Query limit reached. Exiting challenge.")
                break
        except json.JSONDecodeError:
            print({"error": "Invalid JSON format."})
        except Exception as e:
            print(f'{{"error": "An unexpected error occurred: {e}"}}')
            break

if __name__ == "__main__":
    main()


