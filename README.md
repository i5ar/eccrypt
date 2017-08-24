# Easy Crypt

:closed_lock_with_key: Data encryption with RSA key pair.

> If you write books or just some notes, this package will keep your text
safely encrypted.

1. The RSA public key is used to encrypt the session key;
2. The AES session key is used to encrypt the data.

### Requirements:

- Python;
- Node.js (optional);

Since `v0.0.4` it is possible to generate a key pair directly from the menu
bar: `File` > `Generate key pair`.

In BSD Unix-like or GNU/Linux distributions you can easily generate a key pair
using OpenSSH:

    ssh-keygen -t rsa

In Windows you can also generate a key pair using PuTTY.
- Open PuTTYgen;
- Click the Generate button and move the mouse over the blank area;
- Copy your public key from the text area and paste it in a new file
(ex. eccrypt_rsa.pub);
- Open the Conversions submenu and select Export OpenSSH key;
- Save your pivate key (ex. eccrypt_rsa);
- Close PuTTYgen and **keep your private key secret**.

### Installation

Clone the repository, change the current directory and install the
dependencies:

    git clone https://github.com/i5ar/eccrypt.git
    cd eccrypt
    pip install -r requirements.txt

If something goes wrong try to update the package manager:

    python -m pip install --update pip
    pip install -r requirements.txt

### Usage

##### Graphical interface

Since `v0.0.2` is available a simple graphical interface.

> You still need to launch it from the terminal

For the time being, just run `python main.py`.

##### Terminal

Encrypt a text file:

    python manage.py encrypt data/egg.txt --public-key eccrypt_rsa.pub

Decrypt a text file:

    python manage.py decrypt data/egg.bin --private-key eccrypt_rsa

### Note

Original EOL might not be restored depending on your operating system.

### Development

Generate some dummy text in the data directory:

    node loremipsum.js

##### Changelog

- v0.0.4 - Add generate module (RSA key pair);
- v0.0.3 - Improve the graphical interface;
- v0.0.2 - Add a simple graphical interface.

##### TODO

- Try out [loremipsum](https://pypi.python.org/pypi/loremipsum) and eventually
integrate for testing purposes;
- Store the key pair in a database.
