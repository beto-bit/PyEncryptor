# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b_encrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.b_encrypt_btn.setGeometry(QtCore.QRect(230, 160, 101, 23))
        self.b_encrypt_btn.setObjectName("b_encrypt_btn")
        self.b_decrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.b_decrypt_btn.setGeometry(QtCore.QRect(230, 190, 101, 23))
        self.b_decrypt_btn.setObjectName("b_decrypt_btn")
        self.psw_encrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.psw_encrypt_btn.setGeometry(QtCore.QRect(70, 160, 131, 23))
        self.psw_encrypt_btn.setObjectName("psw_encrypt_btn")
        self.psw_decrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.psw_decrypt_btn.setGeometry(QtCore.QRect(70, 190, 131, 23))
        self.psw_decrypt_btn.setObjectName("psw_decrypt_btn")
        self.file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.file_btn.setGeometry(QtCore.QRect(60, 310, 141, 61))
        self.file_btn.setObjectName("file_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 380, 111, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b_encrypt_btn.setText(_translate("MainWindow", "Basic Encryption"))
        self.b_decrypt_btn.setText(_translate("MainWindow", "Basic Decrypt"))
        self.psw_encrypt_btn.setText(_translate("MainWindow", "Password Encryption"))
        self.psw_decrypt_btn.setText(_translate("MainWindow", "Password Decrypt"))
        self.file_btn.setText(_translate("MainWindow", "Open File"))
        self.label.setText(_translate("MainWindow", "Select File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
