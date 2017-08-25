#!/usr/bin/env python
"""Decrypt a text file."""

import os

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP


def decrypt(*args, **kwargs):
    """Decrypt a binary file using a private key.

    The decryption is provided by `PyCryptodome`_.

    Args:
        *args: Input file[s].
        **kwargs: Optional Arbitrary keyword arguments.
            They might represent a RSA private key or the output file[s].

    Examples:
        The first argument is a list while the next argument can be both a
        string or a list, depending on the keyword.

        >>> decrypt(['spam.bin'], rsa_private_key='rsa', output=['spam.text'])

    .. _PyCryptodome:
        https://www.pycryptodome.org

    """
    rsa_private_key = kwargs.get('rsa_private_key')
    for file_input_cipher in enumerate(args):
        filename, file_extension = os.path.splitext(file_input_cipher[1])
        file_input = open(file_input_cipher[1], "rb")

        private_key = RSA.import_key(open(rsa_private_key).read())

        enc_session_key, nonce, tag, ciphertext = [
            file_input.read(x) for x in (
                private_key.size_in_bytes(), 16, 16, -1)]

        file_input.close()

        # Decrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)

        # Decode data
        decoded_data = data.decode("utf-8")

        # Generate the decrypted file
        try:
            file_output = open(kwargs.get('output')[file_input_cipher[0]], "w")
            file_output.write(decoded_data)
            file_output.close()
        except IndexError as e:
            print("Did you provided more input files than output files?", e)
            defout = filename + ".txt"  # Default output :)
            output = input(
                'Enter the next output file[' + defout + ']: ') or defout
            file_output = open(output, "w")
            file_output.write(decoded_data)
            file_output.close()
        except TypeError as e:
            print(file_input_cipher[0], file_input_cipher[1], )
            print(decoded_data)
