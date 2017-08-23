#!/usr/bin/env python
"""Simple GUI for Easy Crypt."""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from encrypt import encrypt
from decrypt import decrypt

interface = tk.Tk()


def open_text_file():
    """Open text file."""
    global text_file_path
    text_file_path = filedialog.askopenfilename()
    print(text_file_path)
    return text_file_path


def open_encrypted_file():
    """Open encrypted file."""
    global encrypted_file_path
    encrypted_file_path = filedialog.askopenfilename()
    print(encrypted_file_path)
    return encrypted_file_path


def open_public_key_file():
    """Open public key file."""
    global public_key_file_path
    public_key_file_path = filedialog.askopenfilename()
    print(public_key_file_path)
    return public_key_file_path


def open_private_key_file():
    """Open private key file."""
    global private_key_file_path
    private_key_file_path = filedialog.askopenfilename()
    print(private_key_file_path)
    return private_key_file_path


def save_encrypted_file():
    """Save encrypted file."""
    f = filedialog.asksaveasfile(mode='wb', defaultextension=".bin")
    if f is None:  # `asksaveasfile` return `None` if dialog closed with Cancel
        return
    try:
        # TODO: Get the data and write the file from here.
        encrypt(
            text_file_path,
            rsa_public_key=public_key_file_path,
            output=f.name)
    except NameError as e:
        print(e)

    # NOTE: Do I need to close the buffered writer?
    f.close()


def save_decrypted_file():
    """Save decrypted file."""
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # `asksaveasfile` return `None` if dialog closed with Cancel
        return
    try:
        # TODO: Get the data and write the file from here.
        decrypt(
            encrypted_file_path,
            rsa_private_key=private_key_file_path,
            output=f.name)
    except NameError as e:
        print(e)

    # NOTE: Do I need to close the buffered writer?
    f.close()


button_open_text_file = ttk.Button(
    interface,
    width=20,
    text="Open text file",
    command=open_text_file)

button_open_encrypted_file = ttk.Button(
    interface,
    width=20,
    state="disabled",
    text="Open encrypted file",
    command=open_encrypted_file)

button_public_key = ttk.Button(
    interface,
    width=20,
    text="Open public key",
    command=open_public_key_file)

button_private_key = ttk.Button(
    interface,
    width=20,
    state="disabled",
    text="Open private key",
    command=open_private_key_file)

button_save_encrypted_file = ttk.Button(
    interface,
    width=20,
    text="Save encrypted file",
    command=save_encrypted_file)

button_save_decrypted_file = ttk.Button(
    interface,
    width=20,
    text="Save decrypted file",
    state="disabled",
    command=save_decrypted_file)

button_open_text_file.grid(column=1, row=2)
button_open_encrypted_file.grid(column=2, row=2)

button_public_key.grid(column=1, row=3)
button_private_key.grid(column=2, row=3)

button_save_encrypted_file.grid(column=1, row=4)
button_save_decrypted_file.grid(column=2, row=4)


def enable_button_public_key(event):
    """Enable encryption buttons."""
    button_public_key.state(["!disabled"])
    button_private_key.state(["disabled"])
    button_open_text_file.state(["!disabled"])
    button_open_encrypted_file.state(["disabled"])
    button_save_encrypted_file.state(["!disabled"])
    button_save_decrypted_file.state(["disabled"])


def enable_button_private_key(event):
    """Enable decryption buttons."""
    button_public_key.state(["disabled"])
    button_private_key.state(["!disabled"])
    button_open_text_file.state(["disabled"])
    button_open_encrypted_file.state(["!disabled"])
    button_save_encrypted_file.state(["disabled"])
    button_save_decrypted_file.state(["!disabled"])


# Radiobuttons
v = tk.StringVar()
v.set("PUB")
radiobutton_public_key = tk.Radiobutton(
    interface,
    width=20,
    text="Encrypt",
    variable=v,
    value="PUB",
    command=lambda: enable_button_public_key(None))
radiobutton_private_key = tk.Radiobutton(
    interface,
    width=20,
    text="Decrypt",
    variable=v,
    value="PRI",
    command=lambda: enable_button_private_key(None))
radiobutton_public_key.grid(column=1, row=1)
radiobutton_private_key.grid(column=2, row=1)


interface.mainloop()
