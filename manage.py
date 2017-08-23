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
parser.add_argument('-o', '--output-file', dest='output', default=None,
                    help='Output file.')

args = parser.parse_args()

crypt = args.crypt  # crypt action
files = args.files  # data files
public = args.public  # public key
private = args.private  # private key
output = args.output  # output file

if crypt == 'encrypt':
    encrypt(*files, rsa_public_key=public, output=output)
elif crypt == 'decrypt':
    decrypt(*files, rsa_private_key=private, output=output)
