# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from pymata4 import pymata4
import time
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(905, 802)
        MainMenu.setAutoFillBackground(False)
        MainMenu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainMenu)
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
        self.logo.setGeometry(QtCore.QRect(20, 10, 411, 131))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("images/header.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.lbl_greeting = QtWidgets.QLabel(self.centralwidget)
        self.lbl_greeting.setGeometry(QtCore.QRect(350, 40, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(22)
        self.lbl_greeting.setFont(font)
        self.lbl_greeting.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.lbl_greeting.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_greeting.setObjectName("lbl_greeting")
        self.btn_suggest_song = QtWidgets.QPushButton(self.centralwidget)
        self.btn_suggest_song.setGeometry(QtCore.QRect(540, 670, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.btn_suggest_song.setFont(font)
        self.btn_suggest_song.setStyleSheet("")
        self.btn_suggest_song.setObjectName("btn_suggest_song")
        self.btn_track_time = QtWidgets.QPushButton(self.centralwidget)
        self.btn_track_time.setGeometry(QtCore.QRect(340, 670, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.btn_track_time.setFont(font)
        self.btn_track_time.setStyleSheet("")
        self.btn_track_time.setObjectName("btn_track_time")
        self.lbl_username = QtWidgets.QLabel(self.centralwidget)
        self.lbl_username.setGeometry(QtCore.QRect(500, 80, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(18)
        self.lbl_username.setFont(font)
        self.lbl_username.setStyleSheet("color:rgba(92,201,107,255);\n"
                                        "background-color: rgba(255, 255, 255, 0);")
        self.lbl_username.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_username.setObjectName("lbl_username")
        self.btn_workout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_workout.setGeometry(QtCore.QRect(140, 670, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.btn_workout.setFont(font)
        self.btn_workout.setStyleSheet("")
        self.btn_workout.setObjectName("btn_workout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 150, 851, 16))
        self.line.setStyleSheet("color:rgba(92,201,107,255);\n"
                                "border-color: rgba(92,201,107,255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.logo_2 = QtWidgets.QLabel(self.centralwidget)
        self.logo_2.setGeometry(QtCore.QRect(830, 40, 61, 61))
        self.logo_2.setText("")
        self.logo_2.setPixmap(QtGui.QPixmap("images/boy.png"))
        self.logo_2.setScaledContents(True)
        self.logo_2.setObjectName("logo_2")
        self.logo_3 = QtWidgets.QLabel(self.centralwidget)
        self.logo_3.setGeometry(QtCore.QRect(40, 180, 821, 331))
        self.logo_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.logo_3.setText("")
        self.logo_3.setPixmap(QtGui.QPixmap("images/plant copy.png"))
        self.logo_3.setScaledContents(True)
        self.logo_3.setObjectName("logo_3")
        self.lbl_greeting_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_greeting_3.setGeometry(QtCore.QRect(130, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(10)
        self.lbl_greeting_3.setFont(font)
        self.lbl_greeting_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.lbl_greeting_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbl_greeting_3.setObjectName("lbl_greeting_3")
        self.lbl_water_level = QtWidgets.QLabel(self.centralwidget)
        self.lbl_water_level.setGeometry(QtCore.QRect(120, 330, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(28)
        self.lbl_water_level.setFont(font)
        self.lbl_water_level.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                           "color: rgb(255, 255, 255);")
        self.lbl_water_level.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_water_level.setObjectName("lbl_water_level")
        self.lbl_greeting_5 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_greeting_5.setGeometry(QtCore.QRect(520, 300, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.lbl_greeting_5.setFont(font)
        self.lbl_greeting_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                          "color: rgb(255, 255, 255);")
        self.lbl_greeting_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_greeting_5.setObjectName("lbl_greeting_5")
        self.lbl_condition = QtWidgets.QLabel(self.centralwidget)
        self.lbl_condition.setGeometry(QtCore.QRect(540, 340, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(28)
        self.lbl_condition.setFont(font)
        self.lbl_condition.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.lbl_condition.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_condition.setObjectName("lbl_condition")
        self.lbl_ai = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ai.setGeometry(QtCore.QRect(70, 490, 771, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.lbl_ai.setFont(font)
        self.lbl_ai.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.lbl_ai.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_ai.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ai.setWordWrap(True)
        self.lbl_ai.setObjectName("lbl_ai")
        self.txt_me = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_me.setGeometry(QtCore.QRect(130, 580, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.txt_me.setFont(font)
        self.txt_me.setObjectName("txt_me")
        self.btn_ask = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ask.setGeometry(QtCore.QRect(690, 580, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.btn_ask.setFont(font)
        self.btn_ask.setStyleSheet("")
        self.btn_ask.setObjectName("btn_ask")
        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 26))
        self.menubar.setObjectName("menubar")
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMenu)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)
        self.btn_ask.clicked.connect(self.chat_bot)
        f = open('user.txt', 'r')
        self.lbl_username.setText(f"{f.read().split(' ')[0]}")

        self.worker = WorkerThread()
        self.worker.start()
        self.worker.update_progress.connect(self.evt_update_progress)

        self.btn_ask.clicked.connect(self.chat_bot)

        self.chatbot = ChatBot('corona bot')

        # Create a new trainer for the chatbot
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)

        # Now let us train our bot with multiple corpus
        self.trainer.train("chatterbot.corpus.english.conversations",
                           "chatterbot.corpus.english.greetings")

    def evt_update_progress(self, val):
        # print(val)
        self.lbl_water_level.setText(f"{val}")
        if val > 650:
            self.lbl_condition.setText("Bad!")
        elif val > 300:
            self.lbl_condition.setText("Avg!")
        else:
            self.lbl_condition.setText("Good!")

    def chat_bot(self):

        response = self.chatbot.get_response(self.txt_me.text())
        print(self.txt_me.text())
        self.lbl_ai.setText(f"{response}")
        self.txt_me.setText(" ")

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Main Menu"))
        self.lbl_greeting.setText(_translate("MainMenu", "Good Evening"))
        self.btn_suggest_song.setText(_translate("MainMenu", "Suggest Me a Song"))
        self.btn_track_time.setText(_translate("MainMenu", "Track My Time"))
        self.lbl_username.setText(_translate("MainMenu", "John Doe"))
        self.btn_workout.setText(_translate("MainMenu", "Workout"))
        self.lbl_greeting_3.setText(_translate("MainMenu", "Water Level"))
        self.lbl_water_level.setText(_translate("MainMenu", "Wait"))
        self.lbl_greeting_5.setText(_translate("MainMenu", "Health of the Plant"))
        self.lbl_condition.setText(_translate("MainMenu", "Wait"))
        self.lbl_ai.setText(_translate("MainMenu", "How are you mate !"))
        self.txt_me.setPlaceholderText(_translate("MainMenu", "Ask me anything!"))
        self.btn_ask.setText(_translate("MainMenu", "ASK"))


class WorkerThread(QThread):
    update_progress = pyqtSignal(int)

    def run(self):
        board = pymata4.Pymata4()

        analog_pin = 0
        digital_pin = 8

        board.set_pin_mode_analog_input(analog_pin)
        board.set_pin_mode_digital_input(digital_pin)

        while True:
            value, time_stamp = board.analog_read(analog_pin)
            # print(value)
            time.sleep(1)
            self.update_progress.emit(value)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec_())
