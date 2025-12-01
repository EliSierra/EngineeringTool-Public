# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
import MainResources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1314, 742)
        MainWindow.setStyleSheet(u"background-color: rgb(179, 191, 213);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Calculatorslbl = QLabel(self.centralwidget)
        self.Calculatorslbl.setObjectName(u"Calculatorslbl")
        self.Calculatorslbl.setMaximumSize(QSize(225, 16777215))
        self.Calculatorslbl.setStyleSheet(u"color: rgb(15, 82, 155);\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.Calculatorslbl, 12, 0, 1, 2)

        self.DataBaseLbl = QLabel(self.centralwidget)
        self.DataBaseLbl.setObjectName(u"DataBaseLbl")
        self.DataBaseLbl.setMaximumSize(QSize(225, 16777215))
        self.DataBaseLbl.setStyleSheet(u"color: rgb(15, 82, 155);\n"
"font-weight: bold;")

        self.gridLayout.addWidget(self.DataBaseLbl, 20, 0, 1, 2)

        self.BeamCall = QPushButton(self.centralwidget)
        self.BeamCall.setObjectName(u"BeamCall")
        self.BeamCall.setMaximumSize(QSize(225, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.BeamCall.setFont(font)
        self.BeamCall.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BeamCall.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.BeamCall, 13, 0, 1, 2)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QSize(225, 16777215))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.pushButton_4, 10, 0, 1, 2)

        self.NewProjectBot = QPushButton(self.centralwidget)
        self.NewProjectBot.setObjectName(u"NewProjectBot")
        sizePolicy.setHeightForWidth(self.NewProjectBot.sizePolicy().hasHeightForWidth())
        self.NewProjectBot.setSizePolicy(sizePolicy)
        self.NewProjectBot.setMaximumSize(QSize(110, 16777215))
        self.NewProjectBot.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.NewProjectBot, 4, 1, 1, 1)

        self.CAMCall = QPushButton(self.centralwidget)
        self.CAMCall.setObjectName(u"CAMCall")
        self.CAMCall.setMaximumSize(QSize(225, 16777215))
        self.CAMCall.setFont(font)
        self.CAMCall.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CAMCall.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.CAMCall, 14, 0, 1, 2)

        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(225, 16777215))
        self.frame_8.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_8.setFrameShape(QFrame.HLine)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_8, 11, 0, 1, 2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(225, 0))
        self.frame_3.setMaximumSize(QSize(225, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_3.setFrameShape(QFrame.HLine)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 19, 0, 1, 2)

        self.UsefulToolslbl = QLabel(self.centralwidget)
        self.UsefulToolslbl.setObjectName(u"UsefulToolslbl")
        self.UsefulToolslbl.setMinimumSize(QSize(225, 0))
        self.UsefulToolslbl.setMaximumSize(QSize(225, 16777215))
        self.UsefulToolslbl.setStyleSheet(u"color: rgb(15, 82, 155);\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.UsefulToolslbl, 6, 0, 1, 2)

        self.OpenProjectBot = QPushButton(self.centralwidget)
        self.OpenProjectBot.setObjectName(u"OpenProjectBot")
        sizePolicy.setHeightForWidth(self.OpenProjectBot.sizePolicy().hasHeightForWidth())
        self.OpenProjectBot.setSizePolicy(sizePolicy)
        self.OpenProjectBot.setMaximumSize(QSize(110, 16777215))
        self.OpenProjectBot.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.OpenProjectBot, 4, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(225, 0))
        self.frame.setMaximumSize(QSize(225, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame.setFrameShape(QFrame.HLine)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame, 5, 0, 1, 2)

        self.KBECall = QPushButton(self.centralwidget)
        self.KBECall.setObjectName(u"KBECall")
        self.KBECall.setMaximumSize(QSize(225, 16777215))
        self.KBECall.setFont(font)
        self.KBECall.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.KBECall.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.KBECall, 22, 0, 1, 2)

        self.ODRIVECall = QPushButton(self.centralwidget)
        self.ODRIVECall.setObjectName(u"ODRIVECall")
        sizePolicy.setHeightForWidth(self.ODRIVECall.sizePolicy().hasHeightForWidth())
        self.ODRIVECall.setSizePolicy(sizePolicy)
        self.ODRIVECall.setMinimumSize(QSize(225, 0))
        self.ODRIVECall.setMaximumSize(QSize(225, 16777215))
        self.ODRIVECall.setFont(font)
        self.ODRIVECall.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.ODRIVECall, 7, 0, 1, 2)

        self.ActiveFile = QLabel(self.centralwidget)
        self.ActiveFile.setObjectName(u"ActiveFile")
        self.ActiveFile.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.ActiveFile, 26, 3, 1, 1)

        self.MaterialCall = QPushButton(self.centralwidget)
        self.MaterialCall.setObjectName(u"MaterialCall")
        self.MaterialCall.setMaximumSize(QSize(225, 16777215))
        self.MaterialCall.setFont(font)
        self.MaterialCall.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.MaterialCall.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.MaterialCall, 21, 0, 1, 2)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(225, 0))
        self.frame_4.setMaximumSize(QSize(225, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_4.setFrameShape(QFrame.HLine)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 3, 0, 1, 2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QSize(225, 16777215))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.pushButton_3, 9, 0, 1, 2)

        self.ImportData = QPushButton(self.centralwidget)
        self.ImportData.setObjectName(u"ImportData")
        self.ImportData.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.ImportData, 14, 5, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(225, 0))
        self.pushButton_2.setMaximumSize(QSize(225, 16777215))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.pushButton_2, 8, 0, 1, 2)

        self.SaveNotes = QPushButton(self.centralwidget)
        self.SaveNotes.setObjectName(u"SaveNotes")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SaveNotes.sizePolicy().hasHeightForWidth())
        self.SaveNotes.setSizePolicy(sizePolicy1)
        self.SaveNotes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SaveNotes.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.SaveNotes, 26, 6, 1, 1)

        self.MainStack = QStackedWidget(self.centralwidget)
        self.MainStack.setObjectName(u"MainStack")
        self.MainStack.setMinimumSize(QSize(870, 638))
        self.MainStack.setMaximumSize(QSize(870, 638))
        self.MainStack.setStyleSheet(u"background-color: rgb(161, 162, 164);\n"
"border-radius: 5px\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.MainStack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.MainStack.addWidget(self.page_2)

        self.gridLayout.addWidget(self.MainStack, 1, 3, 23, 1)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_6.setFrameShape(QFrame.VLine)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_6, 0, 4, 27, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_2.setFrameShape(QFrame.VLine)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_2, 0, 2, 27, 1)

        self.ProjectTitle = QLabel(self.centralwidget)
        self.ProjectTitle.setObjectName(u"ProjectTitle")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.ProjectTitle.setFont(font1)
        self.ProjectTitle.setStyleSheet(u"color: rgb(15, 82, 155);\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.ProjectTitle, 0, 3, 1, 1)

        self.SierraTech = QLabel(self.centralwidget)
        self.SierraTech.setObjectName(u"SierraTech")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SierraTech.sizePolicy().hasHeightForWidth())
        self.SierraTech.setSizePolicy(sizePolicy2)
        self.SierraTech.setMaximumSize(QSize(225, 16777215))
        self.SierraTech.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.SierraTech, 0, 0, 3, 2)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_5.setFrameShape(QFrame.HLine)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_5, 25, 3, 1, 1)

        self.LoadNotes = QPushButton(self.centralwidget)
        self.LoadNotes.setObjectName(u"LoadNotes")
        self.LoadNotes.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.LoadNotes, 25, 5, 1, 1)

        self.SaveNotesAs = QPushButton(self.centralwidget)
        self.SaveNotesAs.setObjectName(u"SaveNotesAs")
        self.SaveNotesAs.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.SaveNotesAs, 25, 6, 1, 1)

        self.ClearNotes = QPushButton(self.centralwidget)
        self.ClearNotes.setObjectName(u"ClearNotes")
        self.ClearNotes.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.ClearNotes, 26, 5, 1, 1)

        self.ClearData = QPushButton(self.centralwidget)
        self.ClearData.setObjectName(u"ClearData")
        self.ClearData.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.ClearData, 14, 6, 1, 1)

        self.RunData = QPushButton(self.centralwidget)
        self.RunData.setObjectName(u"RunData")
        self.RunData.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.RunData, 15, 5, 1, 2)

        self.noteslbl = QLabel(self.centralwidget)
        self.noteslbl.setObjectName(u"noteslbl")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.noteslbl.sizePolicy().hasHeightForWidth())
        self.noteslbl.setSizePolicy(sizePolicy3)
        self.noteslbl.setMinimumSize(QSize(175, 0))
        self.noteslbl.setStyleSheet(u"color: rgb(15, 82, 155);\n"
"font-weight: bold;")

        self.gridLayout.addWidget(self.noteslbl, 17, 5, 1, 2)

        self.Notes = QTextEdit(self.centralwidget)
        self.Notes.setObjectName(u"Notes")
        self.Notes.setStyleSheet(u"background-color: rgb(161, 162, 164);\n"
"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.Notes.setFrameShape(QFrame.Panel)

        self.gridLayout.addWidget(self.Notes, 18, 5, 7, 2)

        self.Metadata = QLabel(self.centralwidget)
        self.Metadata.setObjectName(u"Metadata")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Metadata.sizePolicy().hasHeightForWidth())
        self.Metadata.setSizePolicy(sizePolicy4)
        self.Metadata.setStyleSheet(u"background-color: rgb(161, 162, 164);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px")
        self.Metadata.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.Metadata, 2, 5, 12, 2)

        self.Metadatalbl = QLabel(self.centralwidget)
        self.Metadatalbl.setObjectName(u"Metadatalbl")
        sizePolicy4.setHeightForWidth(self.Metadatalbl.sizePolicy().hasHeightForWidth())
        self.Metadatalbl.setSizePolicy(sizePolicy4)
        self.Metadatalbl.setStyleSheet(u"color: rgb(15, 82, 155);\n"
"font-weight: bold;")

        self.gridLayout.addWidget(self.Metadatalbl, 0, 5, 2, 2)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_7.setFrameShape(QFrame.HLine)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_7, 16, 5, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Calculatorslbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Calculators</span></p></body></html>", None))
        self.DataBaseLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Databases</span></p></body></html>", None))
        self.BeamCall.setText(QCoreApplication.translate("MainWindow", u"Beam Calculator", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Python Guidebook", None))
        self.NewProjectBot.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.CAMCall.setText(QCoreApplication.translate("MainWindow", u"CAM Calculator", None))
        self.UsefulToolslbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Useful Tools</span></p></body></html>", None))
        self.OpenProjectBot.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
        self.KBECall.setText(QCoreApplication.translate("MainWindow", u"KBE", None))
        self.ODRIVECall.setText(QCoreApplication.translate("MainWindow", u"LabView ODRIVE Controller", None))
        self.ActiveFile.setText(QCoreApplication.translate("MainWindow", u"Active Project File: No Project Selected", None))
        self.MaterialCall.setText(QCoreApplication.translate("MainWindow", u"Materials", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Server/Database Guidebook", None))
        self.ImportData.setText(QCoreApplication.translate("MainWindow", u"Import data", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"FEMAP NASTRAN Guidebook", None))
        self.SaveNotes.setText(QCoreApplication.translate("MainWindow", u"Save Notes", None))
        self.ProjectTitle.setText(QCoreApplication.translate("MainWindow", u"No Project Selected", None))
        self.SierraTech.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/Images/Media/SierraTechOG.png\"width=\"225\" /></p></body></html>", None))
        self.LoadNotes.setText(QCoreApplication.translate("MainWindow", u"Load Notes", None))
        self.SaveNotesAs.setText(QCoreApplication.translate("MainWindow", u"Save Notes As", None))
        self.ClearNotes.setText(QCoreApplication.translate("MainWindow", u"Clear Notes", None))
        self.ClearData.setText(QCoreApplication.translate("MainWindow", u"Clear Data", None))
        self.RunData.setText(QCoreApplication.translate("MainWindow", u"Run Data", None))
        self.noteslbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Notes</span></p></body></html>", None))
        self.Metadata.setText("")
        self.Metadatalbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Metadata</span></p></body></html>", None))
    # retranslateUi

