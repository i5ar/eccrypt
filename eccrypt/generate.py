#!/usr/bin/env python
"""Generate RSA key pair."""

from Cryptodome.PublicKey import RSA


def generate(filename="eccrypt_rsa", keytype="rsa"):
    """Generate a key pair based on the RSA algorithm.

    Args:
        filename (str): Name of the key pair.

    """
    if keytype == "rsa":
        key = RSA.generate(2048)
        encrypted_key = key.exportKey()

        file_out_rsa_private_key = open(filename, "wb")
        file_out_rsa_private_key.write(encrypted_key)

        file_out_rsa_public_key = open(filename + ".pub", "wb")
        file_out_rsa_public_key.write(key.publickey().exportKey())

        print(key.publickey().exportKey())
