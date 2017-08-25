Installation
============

Requirements
------------

- Python;

Since v0.0.4 OpenSSH is not required since it is possible to generate a key
pair directly from the menu bar: ``File`` > ``Generate key pair``.

In BSD Unix-like or GNU/Linux distributions you can easily generate a key pair
using OpenSSH::

    ssh-keygen -t rsa

In Windows you can also generate a key pair using PuTTY:

- Open PuTTYgen;
- Click the Generate button and move the mouse over the blank area;
- Copy your public key from the text area and paste it in a new file (ex. eccrypt_rsa.pub);
- Open the Conversions submenu and select Export OpenSSH key;
- Save your pivate key (ex. eccrypt_rsa);
- Close PuTTYgen and **keep your private key secret**.

Installation
------------

Clone the repository, change the current directory and install the
dependencies::

    git clone https://github.com/i5ar/eccrypt.git
    cd eccrypt
    pip install -r requirements.txt

If something goes wrong try to update the package manager::

    python -m pip install --update pip
    pip install -r requirements.txt
