# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import traceback
from main_menu import Ui_MainMenu
from firebase import Firebase
import sys

class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 729)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(42,42,42);\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "border-width:2px;\n"
                                         "border-style:solid;\n"
                                         "border-color: rgb(255, 255, 255);\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::hover\n"
                                         "{\n"
                                         "   \n"
                                         "    color: rgb(30, 30, 30);\n"
                                         "    background-color: rgba(92,201,107,255);\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(340, 30, 311, 301))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(490, 360, 16, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 360, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 360, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.s_first_name = QtWidgets.QLineEdit(self.centralwidget)
        self.s_first_name.setGeometry(QtCore.QRect(170, 410, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.s_first_name.setFont(font)
        self.s_first_name.setStyleSheet("border-color: rgb(56, 54, 54);")
        self.s_first_name.setObjectName("s_first_name")
        self.s_last_name = QtWidgets.QLineEdit(self.centralwidget)
        self.s_last_name.setGeometry(QtCore.QRect(330, 410, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.s_last_name.setFont(font)
        self.s_last_name.setStyleSheet("border-color: rgb(56, 54, 54);")
        self.s_last_name.setObjectName("s_last_name")
        self.s_email = QtWidgets.QLineEdit(self.centralwidget)
        self.s_email.setGeometry(QtCore.QRect(240, 460, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.s_email.setFont(font)
        self.s_email.setStyleSheet("border-color: rgb(56, 54, 54);")
        self.s_email.setObjectName("s_email")
        self.s_user_name = QtWidgets.QLineEdit(self.centralwidget)
        self.s_user_name.setGeometry(QtCore.QRect(240, 510, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.s_user_name.setFont(font)
        self.s_user_name.setStyleSheet("border-color: rgb(56, 54, 54);")
        self.s_user_name.setObjectName("s_user_name")
        self.s_password = QtWidgets.QLineEdit(self.centralwidget)
        self.s_password.setGeometry(QtCore.QRect(240, 560, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.s_password.setFont(font)
        self.s_password.setStyleSheet("border-color: rgb(56, 54, 54);")
        self.s_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.s_password.setObjectName("s_password")
        self.btn_sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign_up.setGeometry(QtCore.QRect(372, 610, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.btn_sign_up.setFont(font)
        self.btn_sign_up.setStyleSheet("")
        self.btn_sign_up.setObjectName("btn_sign_up")
        self.s_user_name_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.s_user_name_2.setGeometry(QtCore.QRect(510, 410, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.s_user_name_2.setFont(font)
        self.s_user_name_2.setStyleSheet("border-color: rgb(56, 54, 54);")
        self.s_user_name_2.setObjectName("s_user_name_2")
        self.l_password = QtWidgets.QLineEdit(self.centralwidget)
        self.l_password.setGeometry(QtCore.QRect(510, 460, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.l_password.setFont(font)
        self.l_password.setStyleSheet("border-color: rgb(56, 54, 54);")
        self.l_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.l_password.setObjectName("l_password")
        self.btn_sign_up_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign_up_2.setGeometry(QtCore.QRect(510, 510, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.btn_sign_up_2.setFont(font)
        self.btn_sign_up_2.setStyleSheet("")
        self.btn_sign_up_2.setObjectName("btn_sign_up_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_sign_up.clicked.connect(self.sign_up)
        self.btn_sign_up_2.clicked.connect(self.login_user)

    def login_user(self):
        email = self.s_user_name_2.text().replace(".","*")
        password = self.l_password.text()
        firebase = Firebase()
        try:
            user_exists = firebase.login_user(email, password)
            if user_exists:
                print('successful')
                self.close()
                # QCoreApplication.instance().quit()
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainMenu()
                self.ui.setupUi(self.window)
                self.window.show()
        except Exception:
            traceback.print_exc()
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("No user found! Try using a different email")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()

    def sign_up(self):
        first_name = self.s_first_name.text()
        last_name = self.s_last_name.text()
        email = self.s_email.text().replace(".","*")
        username = self.s_user_name.text()
        password = self.s_password.text()
        firebase = Firebase()
        try:
            added = firebase.add_user(first_name, last_name, email, username, password)
            if added:
                print('successful')
                self.close()
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainMenu()
                self.ui.setupUi(self.window)
                self.window.show()
        except Exception:
            traceback.print_exc()
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("User already exists! Try using a different email or login")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sign Up"))
        self.label_2.setText(_translate("MainWindow", "Login"))
        self.s_first_name.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.s_last_name.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.s_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.s_user_name.setPlaceholderText(_translate("MainWindow", "UserName"))
        self.s_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.btn_sign_up.setText(_translate("MainWindow", "Sign Up"))
        self.s_user_name_2.setPlaceholderText(_translate("MainWindow", "Email"))
        self.l_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.btn_sign_up_2.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())