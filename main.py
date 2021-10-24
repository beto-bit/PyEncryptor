from ui.mainWindow import Ui_MainWindow
from ui.decryptedTextWindow import Ui_DecryptedWindow

from crypto import basic_encryption, basic_decryption
from crypto import encryption_with_psw, decryption_with_psw
from cryptography.fernet import InvalidToken

import os
import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


class UIFunctionality(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(MainWindow)
        self.setupInteraction()

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
        try:
            encryption_with_psw(
                self.fname, 
                self.psw_edit.toPlainText(),
                self.overwrite_check.isChecked()
            )
            self.output_text("Succeed Encryption")
            self.reset_state()

        except AttributeError:
            self.output_text("ERROR: File or password not selected") 
       
    def psw_decrypt_clicker(self):
        try:
            readonly = self.readonly_check.isChecked()

            decrypted_content = decryption_with_psw(
                self.fname, 
                self.psw_edit.toPlainText(),
                readonly
            )

            # Show in the other window
            if readonly:
                decrypted_text_window.showText(decrypted_content.decode('utf-8'))

            self.output_text("Succeed Decryption")
            self.reset_state()

        except AttributeError:
            self.output_text("ERROR: File or password not selected")
        
        except InvalidToken:
            self.output_text("ERROR: Invalid or Wrong password")

    def b_encrypt_clicker(self):
        try:
            basic_encryption(
                self.fname, 
                self.overwrite_check.isChecked()
            )
            self.output_text("Succeed Basic Encryption")
            self.reset_state()

        except AttributeError:
            self.output_text("ERROR: File not selected")

    def b_decrypt_clicker(self):
        try:
            readonly = self.readonly_check.isChecked()

            decrypted_content = basic_decryption(
                self.fname,
                readonly
            )

            if readonly:
                decrypted_text_window.showText(decrypted_content.decode('utf-8'))

            self.output_text("Succeed Basic Decryption")
            self.reset_state()

        except AttributeError:
            self.output_text("ERROR: File not selected")

    # File Operations
    def file_dialog(self):
        # Create File Dialog.
        fname = QFileDialog.getOpenFileName(
            MainWindow,
            "Select File",
            "",
            "All Files (*)"
        )

        # Check if there is a return value.
        if os.path.isfile(fname[0]):
            self.fname = fname[0]
            
            self.filepath_label.setText(fname[0])
            self.filepath_label.adjustSize()

    # Various Actions
    def output_text(self, text: str):
        """Outputs the text into the output label."""
        self.output_label.setText(' >' + text)

    def reset_state(self):
        """Resets the general state of the program."""
        del self.fname
        
        self.filepath_label.setText("[Selected File]")
        self.filepath_label.adjustSize()

        self.overwrite_check.setChecked(False)
        self.readonly_check.setChecked(False)


class OutputWindow(Ui_DecryptedWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(DecryptedWindow)

    def showText(self, text: str):
        """Shows a text."""
        self.textBrowser.setPlainText(text)
        DecryptedWindow.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    DecryptedWindow = QtWidgets.QWidget()

    ui = UIFunctionality()
    decrypted_text_window = OutputWindow()

    MainWindow.show()
    sys.exit(app.exec_())