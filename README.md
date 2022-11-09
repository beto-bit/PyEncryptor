# PyEncrypter
A program with an integrated GUI, able to encrypt/decrypt various types of files. This is an improved version of the one implemented in Tkinter.
Now it uses ✨real✨ encryption.

### 🖼 GUI
It uses PyQt5 for the GUI.
I choose a dark, high contrast, minimalistic theme (mainly for practical reasons).`

![General View](https://github.com/beto-bit/PyEncryptor/blob/main/.github/images/gui_1.png)

The previous version made use of Tkinter, which was fine, but my experience with programming was generally poor. Also, PyQt5 has the superb GUI editor Qt Designer, which made my life a lot easier.

![Decrypt Window](https://github.com/beto-bit/PyEncryptor/blob/main/.github/images/gui_2.png)

### 🔐 Encrypt/Decrypt
The encryption uses the `cryptography` pip module. It uses Fernet, and is capable of using passwords. Its core functionality makes use of files to store encryption data.
When you use the "Basic Encryption" it generates a `filekey.key` where its stored, well, the key. 
If you decide to use the "Password Encryption" it generates a `salt.key`, which is processed with a human friendly password. 


## 💻 Dev Tools
As it's said, `pyqt5-tools` was used for generating the `.ui` files, making use of Qt Designer (`pyqt5-tools` pip package ships it). I recommend you this [tutorial](https://realpython.com/qt-designer-python/). Then you can transpile them to `.py` ones. There is one PowerShell and one Bash script to transpile both window files. If you're on Mac or GNU/Linux, you should run the script to get the icons working.
If you want to modify the program, I highly recomend you to use a virtual environment. You need to install Qt Designer to modify the `.ui` files.

## 🎊 It's Done
Feel free to share and modify this program. I will thank you a lot. 
