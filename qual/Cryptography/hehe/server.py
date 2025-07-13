import base64
from flask import Flask, request, jsonify
from openfhe import *   # Using version 1.2.3.0.24.4
from secret import FLAG

# Helper functions

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
        pk = DeserializePublicKeyString(bin_str, BINARY)
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


# Main app
app = Flask(__name__)

@app.route("/get-flag", methods=["POST"])
def get_flag():
    """
    ???
    """
    try:
        data = request.get_json()

        # 1. Deserialize CryptoContext, PublicKey, and Ciphertext
        cc_ser = data["crypto_context"]
        cc = deserialize_cc_from_base64(cc_ser)
        assert isinstance(cc, CryptoContext)

        pk_ser = data["public_key"]
        pk = deserialize_pk_from_base64(pk_ser)
        assert isinstance(pk, PublicKey)

        vec_ct_ser = data["ciphertext"]
        vec_ct = deserialize_ct_from_base64(vec_ct_ser)
        assert isinstance(vec_ct, Ciphertext)

        # 2. Add the encrypted FLAG to the encrypted vector
        server_pt = cc.MakePackedPlaintext(FLAG)
        server_ct = cc.Encrypt(pk, server_pt)
        result_ct = cc.EvalAdd(vec_ct, server_ct)

        # 3. Send result
        result_ct_ser = serialize_to_base64(result_ct)

        return jsonify({"encrypted_result": f"{result_ct_ser}"})

    except Exception as e:
        raise RuntimeError(f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)
