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

    python manage.py encrypt data/egg.txt --public-key eccrypt_rsa.pub

Decrypt a file::

    python manage.py decrypt data/egg.bin --private-key eccrypt_rsa
