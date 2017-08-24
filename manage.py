#!/usr/bin/env python
"""Easy encryption and decryption."""

import argparse

from encrypt import encrypt
from decrypt import decrypt

parser = argparse.ArgumentParser(description='AES encryption and decryption.')
parser.add_argument('crypt', choices=['encrypt', 'decrypt'],
                    help='Crypt method.')
parser.add_argument('files', type=str, nargs='+',
                    help='Input file[s].')
parser.add_argument('--public-key', type=str, dest='public',
                    default='eccrypt_rsa.pub',
                    help='RSA public key (default: eccrypt_rsa.pub).')
parser.add_argument('--private-key', type=str, dest='private',
                    default='eccrypt_rsa',
                    help='RSA private key (default: eccrypt_rsa).')
parser.add_argument('-o', '--output-files', dest='output', default=None,
                    nargs='+', help='Output file[s].')

args = parser.parse_args()

crypt = args.crypt  # Crypt action (str)
files = args.files  # Input file[s] (list)
public = args.public  # Public key (str)
private = args.private  # Private key (str)
output = args.output  # Output file[s] (list)

if crypt == 'encrypt':
    encrypt(*files, rsa_public_key=public, output=output)
# NOTE: If `output` not provided do not save the data in a file, print instead.
elif crypt == 'decrypt':
    decrypt(*files, rsa_private_key=private, output=output)
