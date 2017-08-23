#!/usr/bin/env python
"""Encrypt a text file.

https://www.pycryptodome.org/en/latest/src/examples.html#encrypt-data-with-rsa

Because of how the RSA algorithm works it is not possible to encrypt large
files therefore the RSA key is used to encrypt the session key and the AES
session key is used to encrypt the data.
"""

import os

from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP


def encrypt(*args, **kwargs):
    """Encrypt a text file."""
    rsa_public_key = kwargs.get('rsa_public_key')
    for file_data in args:
        filename, file_extension = os.path.splitext(file_data)
        file_out = open(kwargs.get('output') or filename + ".bin", "wb")

        # Get the public key
        recipient_key = RSA.import_key(open(rsa_public_key).read())

        # Generate the random password file
        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        file_out.write(cipher_rsa.encrypt(session_key))

        # Get the data from a text file as byte strings
        file_in = open(file_data, 'rb')
        data = b''.join([line for line in file_in])
        file_in.close()

        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        [file_out.write(x) for x in (cipher_aes.nonce, tag, ciphertext)]
        file_out.close()
