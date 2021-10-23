from ui.mainWindow import Ui_MainWindow
from crypto import basic_encryption, basic_decryption
from crypto import encryption_with_psw, decryption_with_psw

import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


class UI_Functionality(Ui_MainWindow):
    def setupInteraction(self):
        # Buttons
        self.psw_encrypt_btn.clicked.connect(self.psw_encrypt_clicker)
        self.psw_decrypt_btn.clicked.connect(self.psw_decrypt_clicker)
        self.b_encrypt_btn.clicked.connect(self.b_encrypt_clicker)
        self.b_decrypt_btn.clicked.connect(self.b_decrypt_clicker)

        # File operations
        self.file_btn.clicked.connect(self.file_dialog)

        # Password Text Placeholder
        self.psw_edit.setPlaceholderText("Password")

    # Encryption/Decryption operations
    def psw_encrypt_clicker(self):
        try:
            encryption_with_psw(
                self.fname, 
                self.user_psw,
                self.override_check.isChecked()
            )
        except AttributeError:
            print("File or password not selected") 
       
    def psw_decrypt_clicker(self):
        try:
            decryption_with_psw(self.fname, self.user_psw)
        except AttributeError:
            print("File or password not selected")

    def b_encrypt_clicker(self):
        try:
            basic_encryption(
                self.fname, 
                self.override_check.isChecked()
            )
        except AttributeError:
            print("File not selected")

    def b_decrypt_clicker(self):
        try:
            basic_decryption(self.fname)
        except AttributeError:
            print("File not selected")

    # File Operations
    def file_dialog(self):
        # Get password
        self.user_psw = self.psw_edit.toPlainText()

        # Create File Dialog.
        fname = QFileDialog.getOpenFileName(
            MainWindow,
            "Open File",
            "",
            "All Files (*)"
        )

        # Check if there is a return value.
        if fname:
            self.fname = fname[0]
            
            self.label.setText(fname[0])
            self.label.adjustSize()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = UI_Functionality()
    ui.setupUi(MainWindow)
    ui.setupInteraction()

    MainWindow.show()
    sys.exit(app.exec_())