# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MaterialUI.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgb(161, 162, 164);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(15, 82, 155);\n"
"")
        self.frame_5.setFrameShape(QFrame.HLine)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_5, 6, 0, 1, 9)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.label, 1, 2, 1, 3)

        self.Results = QLabel(Form)
        self.Results.setObjectName(u"Results")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Results.sizePolicy().hasHeightForWidth())
        self.Results.setSizePolicy(sizePolicy1)
        self.Results.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px")
        self.Results.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.Results, 4, 1, 1, 7)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 8, 0, 1, 1)

        self.FileSearch = QToolButton(Form)
        self.FileSearch.setObjectName(u"FileSearch")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.FileSearch.sizePolicy().hasHeightForWidth())
        self.FileSearch.setSizePolicy(sizePolicy2)
        self.FileSearch.setStyleSheet(u"background-color: rgb(179, 191, 213);\n"
"border-radius: 5px")

        self.gridLayout.addWidget(self.FileSearch, 8, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 8, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setKerning(True)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 7)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 2)

        self.MaterialAdd = QPushButton(Form)
        self.MaterialAdd.setObjectName(u"MaterialAdd")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.MaterialAdd.sizePolicy().hasHeightForWidth())
        self.MaterialAdd.setSizePolicy(sizePolicy3)
        self.MaterialAdd.setStyleSheet(u"background-color: rgb(179, 191, 213);\n"
"border-radius: 5px")

        self.gridLayout.addWidget(self.MaterialAdd, 8, 7, 1, 1)

        self.FileBar = QLineEdit(Form)
        self.FileBar.setObjectName(u"FileBar")
        sizePolicy3.setHeightForWidth(self.FileBar.sizePolicy().hasHeightForWidth())
        self.FileBar.setSizePolicy(sizePolicy3)
        self.FileBar.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px")

        self.gridLayout.addWidget(self.FileBar, 8, 2, 1, 4)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 9, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.SearchBar = QLineEdit(Form)
        self.SearchBar.setObjectName(u"SearchBar")
        self.SearchBar.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.SearchBar.sizePolicy().hasHeightForWidth())
        self.SearchBar.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(8)
        self.SearchBar.setFont(font2)
        self.SearchBar.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px")

        self.gridLayout.addWidget(self.SearchBar, 2, 2, 1, 4)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 6, 1, 1)

        self.Search = QPushButton(Form)
        self.Search.setObjectName(u"Search")
        sizePolicy3.setHeightForWidth(self.Search.sizePolicy().hasHeightForWidth())
        self.Search.setSizePolicy(sizePolicy3)
        self.Search.setStyleSheet(u"background-color: rgb(179, 191, 213);\n"
"border-radius: 5px")

        self.gridLayout.addWidget(self.Search, 2, 7, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 9, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Material Search", None))
        self.Results.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Upload Materials", None))
        self.FileSearch.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Material Database", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Material Properties", None))
        self.MaterialAdd.setText(QCoreApplication.translate("Form", u"Add Material", None))
        self.Search.setText(QCoreApplication.translate("Form", u"Search", None))
    # retranslateUi

