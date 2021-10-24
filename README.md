# PyEncrypter
A program with an integrated GUI, able to encrypt/decrypt various types of files. This is an improved version of the one implemented in Tkinter.
Now it uses real encryption.

### 🖼 GUI
It uses PyQt5 for the GUI, also using `pyqt5-tools` for transpiling the `.ui` files generated from Qt Designer to `.py` files. 
I choose a dark, high contrast, minimalistic theme (principally for practical reasons).

![General View](https://github.com/beto-bit/PyEncryptor/blob/main/.github/images/gui_1.png)

The use of PyQt5 was a desicion to improve the GUI. The previous version made use of Tkinter, which was fine, but my experience with programming in general was poor.
I choose to use an Object Oriented Pattern to make the interactions (like buttons or labels). Also, PyQt5 has the superb GUI editor Qt Designer, which made my life easier.

![Decrypt Window](https://github.com/beto-bit/PyEncryptor/blob/main/.github/images/gui_2.png)

### 🔐 Encrypt/Decrypt
The encryption uses the `cryptography` pip module. It uses Fernet, and is capable of using passwords. Its core functionality made use of files to store encryption data.
When you use the "Basic Encryption" it generates a `filekey.key` when it is stored, well, the key. 
If you decide to use the "Password Encryption" it generates a `salt.key`, that is processed with a human friendly password. 


## 💻 Dev Tools
As it is said, `pyqt5-tools` was used for transpiling `.ui` files to `.py` ones. There is one PowerShell script to transpile both window files. 
If you want to modify the program, I recomend you to use a virtual environment. You need to install `pyqt5-tools`, and optionally Qt Designer.

## 🎊 It's Done
Feel free to share and modify this program. I will thank you a lot if you do that. 
