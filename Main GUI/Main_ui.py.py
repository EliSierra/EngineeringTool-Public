# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QScrollBar, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
import MainResources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1142, 598)
        MainWindow.setStyleSheet(u"background-color: rgb(179, 191, 213);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.SierraTech = QLabel(self.centralwidget)
        self.SierraTech.setObjectName(u"SierraTech")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SierraTech.sizePolicy().hasHeightForWidth())
        self.SierraTech.setSizePolicy(sizePolicy)
        self.SierraTech.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.SierraTech, 0, 0, 2, 2)

        self.Notes = QTextEdit(self.centralwidget)
        self.Notes.setObjectName(u"Notes")
        self.Notes.setStyleSheet(u"background-color: rgb(161, 162, 164);\n"
"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px\n"
"")
        self.Notes.setFrameShape(QFrame.Panel)

        self.gridLayout.addWidget(self.Notes, 17, 5, 7, 2)

        self.NoteScroll = QScrollBar(self.centralwidget)
        self.NoteScroll.setObjectName(u"NoteScroll")
        self.NoteScroll.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.NoteScroll, 17, 7, 8, 1)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_7.setFrameShape(QFrame.HLine)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_7, 15, 5, 1, 2)

        self.savedatabot = QPushButton(self.centralwidget)
        self.savedatabot.setObjectName(u"savedatabot")
        self.savedatabot.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.savedatabot, 13, 6, 1, 1)

        self.Calculatorslbl = QLabel(self.centralwidget)
        self.Calculatorslbl.setObjectName(u"Calculatorslbl")
        self.Calculatorslbl.setStyleSheet(u"color: rgb(15, 82, 155);\n"
"")

        self.gridLayout.addWidget(self.Calculatorslbl, 11, 0, 1, 2)

        self.MaterialCall = QPushButton(self.centralwidget)
        self.MaterialCall.setObjectName(u"MaterialCall")
        font = QFont()
        font.setPointSize(12)
        self.MaterialCall.setFont(font)
        self.MaterialCall.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.MaterialCall.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.MaterialCall, 21, 0, 1, 2)

        self.ActiveFile = QLabel(self.centralwidget)
        self.ActiveFile.setObjectName(u"ActiveFile")

        self.gridLayout.addWidget(self.ActiveFile, 25, 3, 1, 1)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_5.setFrameShape(QFrame.HLine)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_5, 24, 3, 1, 1)

        self.DataBaseLbl = QLabel(self.centralwidget)
        self.DataBaseLbl.setObjectName(u"DataBaseLbl")
        self.DataBaseLbl.setStyleSheet(u"color: rgb(15, 82, 155);\n"
"")

        self.gridLayout.addWidget(self.DataBaseLbl, 20, 0, 1, 2)

        self.BeamCall = QPushButton(self.centralwidget)
        self.BeamCall.setObjectName(u"BeamCall")
        self.BeamCall.setFont(font)
        self.BeamCall.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BeamCall.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.BeamCall, 12, 0, 1, 2)

        self.SubUIFrame = QFrame(self.centralwidget)
        self.SubUIFrame.setObjectName(u"SubUIFrame")
        sizePolicy.setHeightForWidth(self.SubUIFrame.sizePolicy().hasHeightForWidth())
        self.SubUIFrame.setSizePolicy(sizePolicy)
        self.SubUIFrame.setMinimumSize(QSize(750, 550))
        self.SubUIFrame.setStyleSheet(u"background-color: rgb(161, 162, 164);\n"
"border-radius: 5px\n"
"")
        self.SubUIFrame.setFrameShape(QFrame.StyledPanel)
        self.SubUIFrame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.SubUIFrame, 0, 3, 24, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_2.setFrameShape(QFrame.VLine)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_2, 0, 2, 26, 1)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_6.setFrameShape(QFrame.VLine)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_6, 0, 4, 26, 1)

        self.NewProjectBot = QPushButton(self.centralwidget)
        self.NewProjectBot.setObjectName(u"NewProjectBot")
        self.NewProjectBot.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.NewProjectBot, 3, 1, 1, 1)

        self.SaveNotes = QPushButton(self.centralwidget)
        self.SaveNotes.setObjectName(u"SaveNotes")
        self.SaveNotes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SaveNotes.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.SaveNotes, 25, 5, 1, 2)

        self.Metadatalbl = QLabel(self.centralwidget)
        self.Metadatalbl.setObjectName(u"Metadatalbl")
        self.Metadatalbl.setStyleSheet(u"color: rgb(15, 82, 155);\n"
"")

        self.gridLayout.addWidget(self.Metadatalbl, 0, 5, 1, 3)

        self.CAMCall = QPushButton(self.centralwidget)
        self.CAMCall.setObjectName(u"CAMCall")
        self.CAMCall.setFont(font)
        self.CAMCall.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CAMCall.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.CAMCall, 13, 0, 1, 2)

        self.UsefulToolslbl = QLabel(self.centralwidget)
        self.UsefulToolslbl.setObjectName(u"UsefulToolslbl")
        self.UsefulToolslbl.setStyleSheet(u"color: rgb(15, 82, 155);\n"
"")

        self.gridLayout.addWidget(self.UsefulToolslbl, 5, 0, 1, 2)

        self.OpenProjectBot = QPushButton(self.centralwidget)
        self.OpenProjectBot.setObjectName(u"OpenProjectBot")
        self.OpenProjectBot.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.OpenProjectBot, 3, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame.setFrameShape(QFrame.HLine)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame, 4, 0, 1, 2)

        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_8.setFrameShape(QFrame.HLine)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_8, 10, 0, 1, 2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_3.setFrameShape(QFrame.HLine)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 19, 0, 1, 2)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_4.setFrameShape(QFrame.HLine)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 2, 0, 1, 2)

        self.ODRIVECall = QPushButton(self.centralwidget)
        self.ODRIVECall.setObjectName(u"ODRIVECall")
        self.ODRIVECall.setFont(font)
        self.ODRIVECall.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.ODRIVECall, 6, 0, 1, 2)

        self.KBECall = QPushButton(self.centralwidget)
        self.KBECall.setObjectName(u"KBECall")
        self.KBECall.setFont(font)
        self.KBECall.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.KBECall.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.KBECall, 22, 0, 1, 2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.pushButton, 14, 5, 1, 1)

        self.importdatabot = QPushButton(self.centralwidget)
        self.importdatabot.setObjectName(u"importdatabot")
        self.importdatabot.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.importdatabot, 13, 5, 1, 1)

        self.noteslbl = QLabel(self.centralwidget)
        self.noteslbl.setObjectName(u"noteslbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.noteslbl.sizePolicy().hasHeightForWidth())
        self.noteslbl.setSizePolicy(sizePolicy1)
        self.noteslbl.setMinimumSize(QSize(175, 0))
        self.noteslbl.setStyleSheet(u"color: rgb(15, 82, 155);\n"
"")

        self.gridLayout.addWidget(self.noteslbl, 16, 5, 1, 3)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.pushButton_2, 7, 0, 1, 2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.pushButton_3, 8, 0, 1, 2)

        self.Metadata = QLabel(self.centralwidget)
        self.Metadata.setObjectName(u"Metadata")
        self.Metadata.setStyleSheet(u"background-color: rgb(161, 162, 164);\n"
"border-radius: 5px")
        self.Metadata.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.Metadata, 1, 5, 12, 2)

        self.MetadataScroll = QScrollBar(self.centralwidget)
        self.MetadataScroll.setObjectName(u"MetadataScroll")
        self.MetadataScroll.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.MetadataScroll, 1, 7, 12, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(229, 230, 232);")

        self.gridLayout.addWidget(self.pushButton_4, 9, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SierraTech.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/Images/Media/SierraTechOG.png\"width=\"175\" /></p></body></html>", None))
        self.savedatabot.setText(QCoreApplication.translate("MainWindow", u"Save data", None))
        self.Calculatorslbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Calculators</span></p></body></html>", None))
        self.MaterialCall.setText(QCoreApplication.translate("MainWindow", u"Materials", None))
        self.ActiveFile.setText(QCoreApplication.translate("MainWindow", u"Active Project File:", None))
        self.DataBaseLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Databases</span></p></body></html>", None))
        self.BeamCall.setText(QCoreApplication.translate("MainWindow", u"Beam Calculator", None))
        self.NewProjectBot.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.SaveNotes.setText(QCoreApplication.translate("MainWindow", u"Save Notes", None))
        self.Metadatalbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Metadata</span></p></body></html>", None))
        self.CAMCall.setText(QCoreApplication.translate("MainWindow", u"CAM Calculator", None))
        self.UsefulToolslbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Useful Tools</span></p></body></html>", None))
        self.OpenProjectBot.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
        self.ODRIVECall.setText(QCoreApplication.translate("MainWindow", u"LabView ODRIVE Controller", None))
        self.KBECall.setText(QCoreApplication.translate("MainWindow", u"KBE", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear Data", None))
        self.importdatabot.setText(QCoreApplication.translate("MainWindow", u"Import data", None))
        self.noteslbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Notes</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"FEMAP NASTRAN Guidebook", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Server/Database Guidebook", None))
        self.Metadata.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Python Guidebook", None))
    # retranslateUi

