#!/usr/bin/env python
"""Decrypt a text file."""

import os

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP


def decrypt(*args, **kwargs):
    """Decrypt a text file."""
    rsa_private_key = kwargs.get('rsa_private_key')
    for encrypted_file in args:
        file_in = open(encrypted_file, "rb")

        private_key = RSA.import_key(open(rsa_private_key).read())

        enc_session_key, nonce, tag, ciphertext = [
            file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

        file_in.close()

        # Decrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)

        # Decode data
        decoded_data = data.decode("utf-8")

        # Generate the decrypted file
        if kwargs.get('output'):
            file_out = open(kwargs.get('output'), "w")
            file_out.write(decoded_data)
            file_out.close()
        else:
            print(decoded_data)
