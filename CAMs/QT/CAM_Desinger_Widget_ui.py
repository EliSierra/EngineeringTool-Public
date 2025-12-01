# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CAM_Desinger_Widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_CAMDesigner(object):
    def setupUi(self, CAMDesigner):
        if not CAMDesigner.objectName():
            CAMDesigner.setObjectName(u"CAMDesigner")
        CAMDesigner.resize(750, 567)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CAMDesigner.sizePolicy().hasHeightForWidth())
        CAMDesigner.setSizePolicy(sizePolicy)
        CAMDesigner.setStyleSheet(u"background-color: rgb(161, 162, 164);")
        self.horizontalLayout = QHBoxLayout(CAMDesigner)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_8 = QLineEdit(CAMDesigner)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.lineEdit_8, 16, 6, 1, 1)

        self.lineEdit_10 = QLineEdit(CAMDesigner)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.lineEdit_10, 20, 6, 1, 1)

        self.RiseDegrees = QLineEdit(CAMDesigner)
        self.RiseDegrees.setObjectName(u"RiseDegrees")
        self.RiseDegrees.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.RiseDegrees, 8, 0, 1, 1)

        self.label_3 = QLabel(CAMDesigner)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.TravelRadius = QLineEdit(CAMDesigner)
        self.TravelRadius.setObjectName(u"TravelRadius")
        self.TravelRadius.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.TravelRadius, 4, 0, 1, 1)

        self.FallProfile = QComboBox(CAMDesigner)
        self.FallProfile.addItem("")
        self.FallProfile.addItem("")
        self.FallProfile.addItem("")
        self.FallProfile.addItem("")
        self.FallProfile.setObjectName(u"FallProfile")
        self.FallProfile.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.FallProfile, 20, 0, 1, 1)

        self.label_11 = QLabel(CAMDesigner)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_11, 19, 0, 1, 1)

        self.Triangles = QLineEdit(CAMDesigner)
        self.Triangles.setObjectName(u"Triangles")
        self.Triangles.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.Triangles, 16, 0, 1, 1)

        self.Thickness = QLineEdit(CAMDesigner)
        self.Thickness.setObjectName(u"Thickness")
        self.Thickness.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.Thickness, 6, 0, 1, 1)

        self.label_8 = QLabel(CAMDesigner)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_8, 15, 0, 1, 1)

        self.label_5 = QLabel(CAMDesigner)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)

        self.BaseRadius = QLineEdit(CAMDesigner)
        self.BaseRadius.setObjectName(u"BaseRadius")
        self.BaseRadius.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.BaseRadius, 2, 0, 1, 1)

        self.label_6 = QLabel(CAMDesigner)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_6, 11, 0, 1, 1)

        self.RiseProfile = QComboBox(CAMDesigner)
        self.RiseProfile.addItem("")
        self.RiseProfile.addItem("")
        self.RiseProfile.addItem("")
        self.RiseProfile.addItem("")
        self.RiseProfile.setObjectName(u"RiseProfile")
        self.RiseProfile.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.RiseProfile, 18, 0, 1, 1)

        self.label_10 = QLabel(CAMDesigner)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_10, 17, 0, 1, 1)

        self.HighDwell = QLineEdit(CAMDesigner)
        self.HighDwell.setObjectName(u"HighDwell")
        self.HighDwell.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")
        self.HighDwell.setReadOnly(False)

        self.gridLayout.addWidget(self.HighDwell, 10, 0, 1, 1)

        self.label_17 = QLabel(CAMDesigner)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_17, 11, 6, 1, 1)

        self.STEPBot = QPushButton(CAMDesigner)
        self.STEPBot.setObjectName(u"STEPBot")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.STEPBot.sizePolicy().hasHeightForWidth())
        self.STEPBot.setSizePolicy(sizePolicy1)
        self.STEPBot.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.STEPBot.setStyleSheet(u"background-color: rgb(179, 191, 213);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.STEPBot, 21, 5, 1, 1)

        self.CADBot = QPushButton(CAMDesigner)
        self.CADBot.setObjectName(u"CADBot")
        sizePolicy1.setHeightForWidth(self.CADBot.sizePolicy().hasHeightForWidth())
        self.CADBot.setSizePolicy(sizePolicy1)
        self.CADBot.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CADBot.setStyleSheet(u"background-color: rgb(179, 191, 213);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.CADBot, 21, 3, 1, 1)

        self.label_19 = QLabel(CAMDesigner)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_19, 15, 6, 1, 1)

        self.label_20 = QLabel(CAMDesigner)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_20, 17, 6, 1, 1)

        self.label_18 = QLabel(CAMDesigner)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_18, 13, 6, 1, 1)

        self.lineEdit_2 = QLineEdit(CAMDesigner)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 6, 1, 1)

        self.label_21 = QLabel(CAMDesigner)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_21, 19, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 21, 4, 1, 1)

        self.label_2 = QLabel(CAMDesigner)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_15 = QLabel(CAMDesigner)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_15, 7, 6, 1, 1)

        self.lineEdit_9 = QLineEdit(CAMDesigner)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.lineEdit_9, 18, 6, 1, 1)

        self.label_4 = QLabel(CAMDesigner)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.label_16 = QLabel(CAMDesigner)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_16, 9, 6, 1, 1)

        self.label_7 = QLabel(CAMDesigner)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_7, 13, 0, 1, 1)

        self.FallDegrees = QLineEdit(CAMDesigner)
        self.FallDegrees.setObjectName(u"FallDegrees")
        self.FallDegrees.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.FallDegrees, 12, 0, 1, 1)

        self.LowDwell = QLineEdit(CAMDesigner)
        self.LowDwell.setObjectName(u"LowDwell")
        self.LowDwell.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.LowDwell, 14, 0, 1, 1)

        self.CAMPlot = QFrame(CAMDesigner)
        self.CAMPlot.setObjectName(u"CAMPlot")
        sizePolicy.setHeightForWidth(self.CAMPlot.sizePolicy().hasHeightForWidth())
        self.CAMPlot.setSizePolicy(sizePolicy)
        self.CAMPlot.setFrameShape(QFrame.StyledPanel)
        self.CAMPlot.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.CAMPlot, 1, 1, 20, 5)

        self.label_12 = QLabel(CAMDesigner)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_12, 1, 6, 1, 1)

        self.lineEdit_5 = QLineEdit(CAMDesigner)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.lineEdit_5, 10, 6, 1, 1)

        self.lineEdit_6 = QLineEdit(CAMDesigner)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.lineEdit_6, 12, 6, 1, 1)

        self.lineEdit_7 = QLineEdit(CAMDesigner)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.lineEdit_7, 14, 6, 1, 1)

        self.label_9 = QLabel(CAMDesigner)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 7)

        self.lineEdit_3 = QLineEdit(CAMDesigner)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.lineEdit_3, 6, 6, 1, 1)

        self.lineEdit = QLineEdit(CAMDesigner)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.lineEdit, 2, 6, 1, 1)

        self.lineEdit_4 = QLineEdit(CAMDesigner)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(229, 230, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.lineEdit_4, 8, 6, 1, 1)

        self.label = QLabel(CAMDesigner)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_14 = QLabel(CAMDesigner)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_14, 5, 6, 1, 1)

        self.label_13 = QLabel(CAMDesigner)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_13, 3, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 21, 2, 1, 1)

        self.GraphBot = QPushButton(CAMDesigner)
        self.GraphBot.setObjectName(u"GraphBot")
        sizePolicy1.setHeightForWidth(self.GraphBot.sizePolicy().hasHeightForWidth())
        self.GraphBot.setSizePolicy(sizePolicy1)
        self.GraphBot.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.GraphBot.setStyleSheet(u"background-color: rgb(179, 191, 213);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.GraphBot, 21, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 21, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(734, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 22, 0, 1, 7)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(CAMDesigner)

        QMetaObject.connectSlotsByName(CAMDesigner)
    # setupUi

    def retranslateUi(self, CAMDesigner):
        CAMDesigner.setWindowTitle(QCoreApplication.translate("CAMDesigner", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"Thickness (mm)", None))
        self.FallProfile.setItemText(0, QCoreApplication.translate("CAMDesigner", u"Linear", None))
        self.FallProfile.setItemText(1, QCoreApplication.translate("CAMDesigner", u"Parabolic", None))
        self.FallProfile.setItemText(2, QCoreApplication.translate("CAMDesigner", u"Harmonic", None))
        self.FallProfile.setItemText(3, QCoreApplication.translate("CAMDesigner", u"Cycloidal", None))

        self.label_11.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"Fall Profile", None))
        self.label_8.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"Number of Triangles", None))
        self.label_5.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"Degrees to Dwell", None))
        self.label_6.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"Degrees to Fall", None))
        self.RiseProfile.setItemText(0, QCoreApplication.translate("CAMDesigner", u"Linear", None))
        self.RiseProfile.setItemText(1, QCoreApplication.translate("CAMDesigner", u"Parabolic", None))
        self.RiseProfile.setItemText(2, QCoreApplication.translate("CAMDesigner", u"Harmonic", None))
        self.RiseProfile.setItemText(3, QCoreApplication.translate("CAMDesigner", u"Cycloidal", None))

        self.label_10.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"Rise Profile", None))
        self.label_17.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"TextLabel", None))
        self.STEPBot.setText(QCoreApplication.translate("CAMDesigner", u"Generate STEP", None))
        self.CADBot.setText(QCoreApplication.translate("CAMDesigner", u"Generate CAD", None))
        self.label_19.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"TextLabel", None))
        self.label_21.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"Travel Radius (mm)", None))
        self.label_15.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"Degrees to Rise", None))
        self.label_16.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"Degrees to Dwell", None))
        self.label_12.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("CAMDesigner", u"CAM Designer", None))
        self.label.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"Base Radius (mm)", None))
        self.label_14.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("CAMDesigner", u"\n"
"TextLabel", None))
        self.GraphBot.setText(QCoreApplication.translate("CAMDesigner", u"Generate Graph", None))
    # retranslateUi

