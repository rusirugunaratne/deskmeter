# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'song_suggestion.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import urllib

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
from deepface import DeepFace
import webbrowser
from main_menu import Ui_MainMenu

emotion = ''


class Ui_SongSuggestion(object):
    def __init__(self):
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.imageUpdate)

    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(905, 915)
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
        self.logo.setGeometry(QtCore.QRect(10, 10, 291, 91))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("images/header.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.btn_suggest_song = QtWidgets.QPushButton(self.centralwidget)
        self.btn_suggest_song.setGeometry(QtCore.QRect(210, 790, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.btn_suggest_song.setFont(font)
        self.btn_suggest_song.setStyleSheet("")
        self.btn_suggest_song.setObjectName("btn_suggest_song")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 100, 851, 16))
        self.line.setStyleSheet("color:rgba(92,201,107,255);\n"
                                "border-color: rgba(92,201,107,255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.logo_3 = QtWidgets.QLabel(self.centralwidget)
        self.logo_3.setGeometry(QtCore.QRect(50, 100, 801, 821))
        self.logo_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.logo_3.setText("")
        self.logo_3.setPixmap(QtGui.QPixmap("images/music.png"))
        self.logo_3.setScaledContents(True)
        self.logo_3.setObjectName("logo_3")
        self.lbl_mood = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mood.setGeometry(QtCore.QRect(140, 620, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.lbl_mood.setFont(font)
        self.lbl_mood.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(255, 255, 255);")
        self.lbl_mood.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mood.setObjectName("lbl_mood")
        self.btn_home = QtWidgets.QPushButton(self.centralwidget)
        self.btn_home.setGeometry(QtCore.QRect(750, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setObjectName("btn_home")
        self.txt_artist = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_artist.setGeometry(QtCore.QRect(590, 630, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        self.txt_artist.setFont(font)
        self.txt_artist.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgba(255, 255, 255, 0);\n"
                                      "border-color: rgb(0, 255, 255);\n"
                                      "")
        self.txt_artist.setObjectName("txt_artist")
        self.lbl_video = QtWidgets.QLabel(self.centralwidget)
        self.lbl_video.setGeometry(QtCore.QRect(100, 150, 701, 511))
        self.lbl_video.setText("")
        self.lbl_video.setObjectName("lbl_video")
        self.lbl_video.raise_()
        self.logo.raise_()
        self.line.raise_()
        self.logo_3.raise_()
        self.lbl_mood.raise_()
        self.btn_home.raise_()
        self.btn_suggest_song.raise_()
        self.txt_artist.raise_()
        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 26))
        self.menubar.setObjectName("menubar")
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMenu)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.btn_home.clicked.connect(self.open_main_menu)
        self.btn_suggest_song.clicked.connect(self.search_song)
        self.lbl_mood.setText(emotion)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def search_song(self):
        query = emotion + ' songs by ' + self.txt_artist.text()
        query = urllib.parse.quote(query)
        url = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(url)
        print(url)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Main Menu"))
        self.btn_suggest_song.setText(_translate("MainMenu", "Suggest Me a Song"))
        self.lbl_mood.setText(_translate("MainMenu", emotion))
        self.btn_home.setText(_translate("MainMenu", "Home"))
        self.txt_artist.setPlaceholderText(_translate("MainMenu", "Charlie Puth"))

    def imageUpdate(self, Image):
        self.lbl_video.setPixmap(QPixmap.fromImage(Image))

    def open_main_menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self.window)
        self.window.show()
        self.Worker1.stop()
        self.close()

    def cancelFeed(self):
        self.Worker1.stop()
        self.close()


class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:

            # Capture.release()
            ret, frame = Capture.read()

            #
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
            # cv2.imshow('frame', frame)
            result = DeepFace.analyze(frame, actions=['emotion'], detector_backend=backends[1], enforce_detection=False)
            global emotion
            emotion = result['dominant_emotion']
            if emotion == 'neutral' or emotion == 'angry' or emotion == 'sad':
                emotion = 'happy'
            print(emotion)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,
                        result['dominant_emotion'],
                        (100, 100),
                        font, 3,
                        (0, 0, 255),
                        2,
                        cv2.LINE_4
                        )

            #

            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = Image
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0],
                                           QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(700, 525)
                self.ImageUpdate.emit(Pic)

        Capture.release()

    def stop(self):
        self.ThreadActive = False
        self.quit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QMainWindow()
    ui = Ui_SongSuggestion()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec_())
