from ui.mainWindow import Ui_MainWindow
from crypto import basic_encryption, basic_decryption
from crypto import encryption_with_psw, decryption_with_psw

import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget


class UI_Functionality(Ui_MainWindow):
    def setupInteraction(self):
        # Buttons
        self.psw_encrypt_btn.clicked.connect(self.psw_encrypt_clicker)
        self.psw_decrypt_btn.clicked.connect(self.psw_decrypt_clicker)
        self.b_encrypt_btn.clicked.connect(self.b_encrypt_clicker)
        self.b_decrypt_btn.clicked.connect(self.b_decrypt_clicker)

        # File operations
        self.file_btn.clicked.connect(self.file_dialog)

    # Encryption/Decryption operations
    def psw_encrypt_clicker(self):
        if self.fname:
            encryption_with_psw(self.fname, "admin",)

    def psw_decrypt_clicker(self):
        if self.fname:
            decryption_with_psw(self.fname, "admin")

    def b_encrypt_clicker(self):
        if self.fname:
            basic_encryption(self.fname)

    def b_decrypt_clicker(self):
        if self.fname:
            basic_decryption(self.fname)

    # File Operations
    def file_dialog(self):
        fname = QFileDialog.getOpenFileName(
            mw,
            "Open File",
            "",
            "All Files (*)"
        )

        if fname:
            self.fname = fname[0]
            
            self.label.setText(fname[0])
            self.label.adjustSize()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QtWidgets.QMainWindow()

    ui = UI_Functionality()
    ui.setupUi(mw)
    ui.setupInteraction()

    mw.show()
    sys.exit(app.exec_())