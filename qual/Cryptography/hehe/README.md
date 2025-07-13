# HE

## Author

k1nomi

## Categories

Cryptography

## Description

Homomorphic Encryption (HE) is a form of encryption that allows computations to be performed on encrypted data without first having to decrypt it. This challenge is a simple implementation of HE where you just need to "get" the flag from the server by implementing a "BFVRNS" scheme using Python's openFHE library (version 1.2.3.0.24.4).

https://xx.xx.xx.xx:yyyy (POST request only)

## Solver

- Reverse code dari `server.py`
- Pelajari tentang openFHE dari dokumentasi dan chatGPT :)

```py
from typing import List, Dict, Union
import base64
import requests
from openfhe import *

# Helper Functions from Server

def serialize_to_base64(obj):
	"""
	Takes  any FHE  object and  turns it into 
	base64.
	"""
	try:
		ser = Serialize(obj, BINARY)
		base64_str = base64.b64encode(ser).decode("utf-8")
		return base64_str
	except Exception as e:
		raise RuntimeError(f"Error: {e}")


def deserialize_cc_from_base64(cc_ser):
	"""
	Takes  base64  and   turns  it  into  FHE 
	CryptoContext object.
	"""
	try:
		bin_str = base64.b64decode(cc_ser)
		cc = DeserializeCryptoContextString(bin_str, BINARY)
		return cc
	except Exception as e:
		raise RuntimeError(f"Error: {e}")


def deserialize_pk_from_base64(pk_ser):
	"""
	Takes  base64  and   turns  it  into  FHE 
	PublicKey object.
	"""
	try:
		bin_str = base64.b64decode(pk_ser)
		pk = DeserializeCryptoContextString(bin_str, BINARY)
		return pk
	except Exception as e:
		raise RuntimeError(f"Error: {e}")


def deserialize_ct_from_base64(ct_ser):
	"""
	Takes  base64  and   turns  it  into  FHE 
	Ciphertext object.
	"""
	try:
		bin_str = base64.b64decode(ct_ser)
		ct = DeserializeCiphertextString(bin_str, BINARY)
		return ct
	except Exception as e:
		raise RuntimeError(f"Error: {e}")


# Main Functions

def BFVRNS_init(ptmod=65537, muld=2):
	"""
	Returns CryptoContext and keys.
	"""
	try:
		# Step 1: Set encryption parameters
		params = CCParamsBFVRNS()
		params.SetPlaintextModulus(ptmod)  		# Must be a prime number
		params.SetMultiplicativeDepth(muld)   	# Controls number of ops before noise overflows

		# Step 2: Generate crypto context (Public Key Encyrption, Leveled SHE)
		cc = GenCryptoContext(params)
		cc.Enable(PKESchemeFeature.PKE)
		cc.Enable(PKESchemeFeature.LEVELEDSHE)

		# Step 3: Key generation
		keys = cc.KeyGen()
		cc.EvalMultKeyGen(keys.secretKey)		# For multiplication

		return cc, keys

	except Exception as e:
		raise RuntimeError(f"Error: {e}")


def BFVRNS_encrypt_vec(cc, pk, vec: List[int]) -> Ciphertext:
	"""
	Returns an encrypted vector
	"""
	try:
		vec_pt = cc.MakePackedPlaintext(vec)
		vec_ct = cc.Encrypt(pk, vec_pt)
		return vec_ct

	except Exception as e:
		raise RuntimeError(f"Error: {e}")


def BFVRNS_decrypt_vec(cc, sk, vec_ct) -> List:
	"""
	Returns a decrypted vector
	"""
	try:
		vec_pt = cc.Decrypt(sk, vec_ct)
		vec = vec_pt.GetPackedValue()
		return vec

	except Exception as e:
		raise RuntimeError(f"Error: {e}")


# Main logic

vec = [0 for _ in range(128)]

def get_flag(vec: List, server_url: str) -> List:
	"""
	Sends a vector to the server to be added with SERVER_VAL
	"""
	try:
		# 1. Encrypt vector
		cc, keys = BFVRNS_init()
		vec_ct = BFVRNS_encrypt_vec(cc, keys.publicKey, vec)

		# 2. Send to server & get encrypted results
		payload = {
			"crypto_context": serialize_to_base64(cc),
			"public_key": serialize_to_base64(keys.publicKey),
			"ciphertext": serialize_to_base64(vec_ct),	
		}
		result = requests.post(server_url + "/get-flag", json=payload)
		result_ct_ser = result.json()["encrypted_result"]

		# 3. Decrypt result
		result_ct = deserialize_ct_from_base64(result_ct_ser)
		result = cc.Decrypt(keys.secretKey, result_ct)
		result_vec = result.GetPackedValue()	# Default length: 8192

		return result_vec

	except Exception as e:
		raise RuntimeError(f"Error: {e}")

msg = get_flag(vec, "http://127.0.0.1:5000")
flag = "".join([chr(i) for i in msg])

print(flag)
```

## Flag

```
ITFEST25{HE_c4n_b3_us3d_t0_pr0t3ct_d4t4_pr1v4cy_0n_ML_m0d3ls}
```
