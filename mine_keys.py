#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys
from hashlib import sha512
 
import base58
import rsakey
import enc
import mbase32
 
import re
 
if len(sys.argv) > 1:
    rx = re.compile(sys.argv[1])
else:
    rx = re.compile('.+')
 
while True:
    key = rsakey.RsaKey.generate(bits=4096)
    k32 = mbase32.encode(enc.generate_ID(key.asbytes()))
    if rx.match(k32):
        print("---")
        print("priv: " + base58.encode(key._encode_key()))
        print("key:  " + k32)
