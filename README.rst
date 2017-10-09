==========
Easy Crypt
==========

Data encryption with RSA key pair.

    If you need to store some confidential text — this package will keep your
    data safely encrypted.
    No more leaks!

This project is built on top of PyCryptodome_ and aim to provide an easy and
accessible interface.

1. The RSA public key is used to encrypt the session key;
2. The AES session key is used to encrypt the data.

Installation
============

Requirements
------------

- Python;


In BSD Unix or GNU/Linux distributions you can easily generate a key pair
using OpenSSH::

    ssh-keygen -t rsa
    ssh-keygen -y -f eccrypt_rsa > eccrypt_rsa.pub  # if you have a private one

In Windows you can also generate a key pair using PuTTY:

- Open PuTTYgen;
- Click the Generate button and move the mouse over the blank area;
- Copy your public key from the text area and paste it in a new file (ex. eccrypt_rsa.pub);
- Open the Conversions submenu and select Export OpenSSH key;
- Save your pivate key (ex. eccrypt_rsa);
- Close PuTTYgen and **keep your private key secret**.

Since v0.0.4 it is possible to generate a key pair directly from the menu
bar: ``File`` > ``Generate key pair``.

Installation
------------

Clone the repository, change the current directory and install the
dependencies::

    git clone https://github.com/i5ar/eccrypt.git
    cd eccrypt
    python setup.py install

If something goes wrong try to update the package manager::

    python -m pip install --update pip
    pip install -r requirements.txt

Quickstart
==========

Graphical interface
-------------------

Since v0.0.2 it is available a simple graphical interface.

    You still need to launch it from the terminal.

For the time being, just run ``python main.py``.

Terminal
--------

Encrypt a file::

    eccrypt encrypt data/egg.txt --public-key eccrypt_rsa.pub

Decrypt a file::

    eccrypt decrypt data/egg.bin --private-key eccrypt_rsa

Note
====

Original EOL might not be restored depending on your operating system.

Development
===========

Generate some dummy text in the data directory::

    node loremipsum.js

Create a source distribution::

    python setup.py sdist

create built distributions::

    python setup.py bdist_wininst  # Windows
    python setup.py bdist_rpm  # RPM-based system

Documentation
-------------

Add new *docstrings* to the API documentation::

    make clean -C ./docs  # remove previous build
    sphinx-apidoc -o docs eccrypt -f  # force override
    make html -C ./docs  # build

Changelog
---------

- v0.0.6 - Add command line script;
- v0.0.5 - Add documentation;
- v0.0.4 - Add generate module (RSA key pair);
- v0.0.3 - Improve the graphical interface;
- v0.0.2 - Add a simple graphical interface.

TODO
----

- Try out loremipsum_ and eventually integrate for testing purposes;
- Store the key pair in a database;
- Apparently, I need to come up with a hook for the installer.


.. _loremipsum: https://pypi.python.org/pypi/loremipsum
.. _PyCryptodome:
    https://www.pycryptodome.org
