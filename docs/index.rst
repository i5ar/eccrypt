.. Easy Crypt documentation master file, created by
   sphinx-quickstart on Mon Oct 2 21:44:09 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Easy Crypt's documentation!
======================================

Data encryption with RSA key pair.

    If you write for *secret services*  — or just need to store some
    confidential text — this package will keep your data safely encrypted.
    No more leaks!

This project is built on top of PyCryptodome_ and aim to provide an easy and
accessible interface.

1. The RSA public key is used to encrypt the session key;
2. The AES session key is used to encrypt the data.

.. _PyCryptodome: https://www.pycryptodome.org


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
