#!/usr/bin/env python
"""Simple GUI for Easy Crypt."""

import tkinter as tk
# from tkinter import ttk
from tkinter import filedialog

from encrypt import encrypt
from decrypt import decrypt
from tkinter import messagebox

__version__ = "0.0.3-alpha"


# Solarized colorscheme
base03 = "#002b36"
base02 = "#073642"
base01 = "#586e75"
base00 = "#657b83"
base0 = "#839496"
base1 = "#93a1a1"
base2 = "#eee8d5"
base3 = "#fdf6e3"
yellow = "#b58900"
orange = "#cb4b16"
red = "#dc322f"
magenta = "#d33682"
violet = "#6c71c4"
blue = "#268bd2"
cyan = "#2aa198"
green = "#859900"


class EasyButtons:
    """Easy Buttons."""

    def __init__(self, master):
        """."""
        frame = tk.Frame(master)
        frame.pack()
        # frame.configure(background=base03)

        self.text_file_paths = None
        self.encrypted_file_paths = None
        self.public_key_file_path = None
        self.private_key_file_path = None

        # Radiobuttons
        self.v = tk.StringVar()
        self.v.set("PUB")

        self.radiobutton_public_key = tk.Radiobutton(
            frame,
            width=20,
            text="Encrypt",
            variable=self.v,
            value="PUB",
            # bg=base03,
            command=lambda: self.enable_button_public_key(None))
        self.radiobutton_public_key.grid(column=1, row=1, padx=20, pady=20)

        self.radiobutton_private_key = tk.Radiobutton(
            frame,
            width=20,
            text="Decrypt",
            variable=self.v,
            value="PRI",
            # bg=base03,
            command=lambda: self.enable_button_private_key(None))
        self.radiobutton_private_key.grid(column=2, row=1, padx=20, pady=20)

        # Buttons
        self.button_open_text_file = tk.Button(
            frame,
            width=20,
            text="Open text file",
            relief=tk.GROOVE,
            # bg=base01,
            command=self.open_text_file)
        # self.button_open_text_file.pack(side=tk.LEFT)
        self.button_open_text_file.grid(column=1, row=2, padx=5, pady=5)

        self.button_open_encrypted_file = tk.Button(
            frame,
            width=20,
            state=tk.DISABLED,  # Use "disabled" in `ttk`
            text="Open encrypted file",
            relief=tk.GROOVE,
            # bg=base01,
            command=self.open_encrypted_file)
        self.button_open_encrypted_file.grid(column=2, row=2, padx=5, pady=5)

        self.button_public_key = tk.Button(
            frame,
            width=20,
            text="Open public key",
            relief=tk.GROOVE,
            # bg=base01,
            command=self.open_public_key_file)
        self.button_public_key.grid(column=1, row=3, padx=5, pady=5)

        self.button_private_key = tk.Button(
            frame,
            width=20,
            state=tk.DISABLED,  # Use "disabled" in `ttk`
            text="Open private key",
            relief=tk.GROOVE,
            # bg=base01,
            command=self.open_private_key_file)
        self.button_private_key.grid(column=2, row=3, padx=5, pady=5)

        self.button_save_encrypted_file = tk.Button(
            frame,
            width=20,
            text="Save encrypted file",
            relief=tk.GROOVE,
            # bg=base01,
            command=self.save_encrypted_file)
        self.button_save_encrypted_file.grid(column=1, row=4, padx=20, pady=20)

        self.button_save_decrypted_file = tk.Button(
            frame,
            width=20,
            text="Save decrypted file",
            relief=tk.GROOVE,
            # bg=base01,
            state=tk.DISABLED,  # Use "disabled" in `ttk`
            command=self.save_decrypted_file)
        self.button_save_decrypted_file.grid(column=2, row=4, padx=20, pady=20)

    def enable_button_public_key(self, event):
        """Enable encryption buttons."""
        # NOTE: Use `state` attribute with `ttk` buttons
        # self.button_public_key.state(["!disabled"])
        # self.button_private_key.state(["disabled"])
        # self.button_open_text_file.state(["!disabled"])
        # self.button_open_encrypted_file.state(["disabled"])
        # self.button_save_encrypted_file.state(["!disabled"])
        # self.button_save_decrypted_file.state(["disabled"])
        # NOTE: Use `state` key with `tk` buttons
        self.button_public_key['state'] = tk.NORMAL
        self.button_private_key['state'] = tk.DISABLED
        self.button_open_text_file['state'] = tk.NORMAL
        self.button_open_encrypted_file['state'] = tk.DISABLED
        self.button_save_encrypted_file['state'] = tk.NORMAL
        self.button_save_decrypted_file['state'] = tk.DISABLED

    def enable_button_private_key(self, event):
        """Enable decryption buttons."""
        # NOTE: Use `state` attribute with `ttk` buttons
        # self.button_public_key.state(["disabled"])
        # self.button_private_key.state(["!disabled"])
        # self.button_open_text_file.state(["disabled"])
        # self.button_open_encrypted_file.state(["!disabled"])
        # self.button_save_encrypted_file.state(["disabled"])
        # self.button_save_decrypted_file.state(["!disabled"])
        # NOTE: Use `state` key with `tk` buttons
        self.button_public_key['state'] = tk.DISABLED
        self.button_private_key['state'] = tk.NORMAL
        self.button_open_text_file['state'] = tk.DISABLED
        self.button_open_encrypted_file['state'] = tk.NORMAL
        self.button_save_encrypted_file['state'] = tk.DISABLED
        self.button_save_decrypted_file['state'] = tk.NORMAL

    def open_text_file(self):
        """Open text file."""
        self.text_file_paths = filedialog.askopenfilenames()
        print(self.text_file_paths)
        return self.text_file_paths

    def open_encrypted_file(self):
        """Open encrypted file."""
        self.encrypted_file_paths = filedialog.askopenfilenames()
        print(self.encrypted_file_paths)
        return self.encrypted_file_paths

    def open_public_key_file(self):
        """Open public key file."""
        self.public_key_file_path = filedialog.askopenfilename()
        print(self.public_key_file_path)
        return self.public_key_file_path

    def open_private_key_file(self):
        """Open private key file."""
        self.private_key_file_path = filedialog.askopenfilename()
        print(self.private_key_file_path)
        return self.private_key_file_path

    def save_encrypted_file(self):
        """Save encrypted file."""
        f = filedialog.asksaveasfile(mode='wb', defaultextension=".bin")
        # Method `asksaveasfile` return `None` if dialog closed with "Cancel".
        if f is None:
            return
        try:
            # TODO: Remove `output` and write the file from here.
            encrypt(
                ' '.join(self.text_file_paths),  # Convert tuple to string
                rsa_public_key=self.public_key_file_path,
                output=f.name)
        except NameError as e:
            print(e)

        # NOTE: Do I need to close the buffered writer?
        f.close()

    def save_decrypted_file(self):
        """Save decrypted file."""
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        # Method `asksaveasfile` return `None` if dialog closed with "Cancel".
        if f is None:
            return
        try:
            # TODO: Remove `output` and write the file from here.
            decrypt(
                ' '.join(self.encrypted_file_paths),  # Convert tuple to string
                rsa_private_key=self.private_key_file_path,
                output=f.name)
        except NameError as e:
            print(e)

        # NOTE: Do I need to close the buffered writer?
        f.close()


root = tk.Tk()
b = EasyButtons(root)


# Menu bar
def save_configuration():
    """Save configuration from menu."""
    messagebox.showwarning(
        "Save", "This function is not yet available. Sorry!")


def show_about():
    """Show about from menu."""
    messagebox.showinfo(
        "About", "Easy Crypt v" + __version__ + " \nArch. Pierpaolo Rasicci")


menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=save_configuration)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=show_about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


# Status bar
status = tk.Label(
    root,
    text="Non men che saver, dubbiar m'aggrata.",
    bd=1,
    relief=tk.SUNKEN,
    anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

# Title
root.title("Easy Crypt")

# Main loop
root.mainloop()
