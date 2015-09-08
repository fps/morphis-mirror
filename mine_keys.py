import base58
import rsakey
import enc
from hashlib import sha512
import mbase32

while True:
    print("---")
    key = rsakey.RsaKey.generate(bits=4096)
    print("priv:" + base58.encode(key._encode_key()))
    print("key: " + mbase32.encode(enc.generate_ID(key.asbytes())))
