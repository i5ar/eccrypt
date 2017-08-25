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
    """
    Encrypt a text file using a public key.
    The encryption is provided by `PyCryptodome`_.

    Args:
        *args: Input file[s].
        **kwargs: Optional Arbitrary keyword arguments.
            They might represent a RSA public key or the output file[s].

    Examples:
        The first argument is a list while the next argument can be both a
        string or a list, depending on the keyword.

        >>> encrypt(['egg.txt'], rsa_public_key='rsa.pub', output=['egg.bin'])

    .. _PyCryptodome:
        https://www.pycryptodome.org

    """
    rsa_public_key = kwargs.get('rsa_public_key')
    for file_input_plain in enumerate(args):
        filename, file_extension = os.path.splitext(file_input_plain[1])
        defout = filename + ".bin"  # Default output :)
        try:
            file_output = open(
                kwargs.get(
                    'output')[file_input_plain[0]] or defout, "wb")
        except IndexError as e:
            print("Did you provided more input files than output files?", e)
            output = input(
                'Enter the next output file[' + defout + ']: ') or defout
            file_output = open(output, "wb")
        except TypeError as e:
            print("Probably you didn't provided an output:", e)
            # The output file will be in the same directory of the input file.
            file_output = open(defout, "wb")

        # Get the public key
        recipient_key = RSA.import_key(open(rsa_public_key).read())

        # Generate the random password file
        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        file_output.write(cipher_rsa.encrypt(session_key))

        # Get the data from a text file as byte strings
        file_in = open(file_input_plain[1], 'rb')
        data = b''.join([line for line in file_in])
        file_in.close()

        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        [file_output.write(x) for x in (cipher_aes.nonce, tag, ciphertext)]
        file_output.close()
