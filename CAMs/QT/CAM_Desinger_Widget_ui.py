# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CAM_Desinger_Widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
## CONVERTED from PySide6 to PyQt6 for framework consistency
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_CAMDesigner(object):
    def setupUi(self, CAMDesigner):
        if not CAMDesigner.objectName():
            CAMDesigner.setObjectName(u"CAMDesigner")
        CAMDesigner.resize(750, 567)
        # Flexible sizing - allow expansion instead of fixed
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CAMDesigner.sizePolicy().hasHeightForWidth())
        CAMDesigner.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(CAMDesigner)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_8 = QLineEdit(CAMDesigner)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 16, 6, 1, 1)

        self.lineEdit_10 = QLineEdit(CAMDesigner)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout.addWidget(self.lineEdit_10, 20, 6, 1, 1)

        self.RiseDegrees = QLineEdit(CAMDesigner)
        self.RiseDegrees.setObjectName(u"RiseDegrees")

        self.gridLayout.addWidget(self.RiseDegrees, 8, 0, 1, 1)

        self.label_3 = QLabel(CAMDesigner)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.TravelRadius = QLineEdit(CAMDesigner)
        self.TravelRadius.setObjectName(u"TravelRadius")

        self.gridLayout.addWidget(self.TravelRadius, 4, 0, 1, 1)

        self.FallProfile = QComboBox(CAMDesigner)
        self.FallProfile.addItem("")
        self.FallProfile.addItem("")
        self.FallProfile.addItem("")
        self.FallProfile.addItem("")
        self.FallProfile.setObjectName(u"FallProfile")

        self.gridLayout.addWidget(self.FallProfile, 20, 0, 1, 1)

        self.label_11 = QLabel(CAMDesigner)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 19, 0, 1, 1)

        self.Triangles = QLineEdit(CAMDesigner)
        self.Triangles.setObjectName(u"Triangles")

        self.gridLayout.addWidget(self.Triangles, 16, 0, 1, 1)

        self.Thickness = QLineEdit(CAMDesigner)
        self.Thickness.setObjectName(u"Thickness")

        self.gridLayout.addWidget(self.Thickness, 6, 0, 1, 1)

        self.label_8 = QLabel(CAMDesigner)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 15, 0, 1, 1)

        self.label_5 = QLabel(CAMDesigner)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)

        self.BaseRadius = QLineEdit(CAMDesigner)
        self.BaseRadius.setObjectName(u"BaseRadius")

        self.gridLayout.addWidget(self.BaseRadius, 2, 0, 1, 1)

        self.label_6 = QLabel(CAMDesigner)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 11, 0, 1, 1)

        self.RiseProfile = QComboBox(CAMDesigner)
        self.RiseProfile.addItem("")
        self.RiseProfile.addItem("")
        self.RiseProfile.addItem("")
        self.RiseProfile.addItem("")
        self.RiseProfile.setObjectName(u"RiseProfile")

        self.gridLayout.addWidget(self.RiseProfile, 18, 0, 1, 1)

        self.label_10 = QLabel(CAMDesigner)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 17, 0, 1, 1)

        self.HighDwell = QLineEdit(CAMDesigner)
        self.HighDwell.setObjectName(u"HighDwell")
        self.HighDwell.setReadOnly(False)

        self.gridLayout.addWidget(self.HighDwell, 10, 0, 1, 1)

        self.label_17 = QLabel(CAMDesigner)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 11, 6, 1, 1)

        self.STEPBot = QPushButton(CAMDesigner)
        self.STEPBot.setObjectName(u"STEPBot")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.STEPBot.sizePolicy().hasHeightForWidth())
        self.STEPBot.setSizePolicy(sizePolicy1)
        self.STEPBot.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.STEPBot, 21, 5, 1, 1)

        self.CADBot = QPushButton(CAMDesigner)
        self.CADBot.setObjectName(u"CADBot")
        sizePolicy1.setHeightForWidth(self.CADBot.sizePolicy().hasHeightForWidth())
        self.CADBot.setSizePolicy(sizePolicy1)
        self.CADBot.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.CADBot, 21, 3, 1, 1)

        self.label_19 = QLabel(CAMDesigner)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 15, 6, 1, 1)

        self.label_20 = QLabel(CAMDesigner)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 17, 6, 1, 1)

        self.label_18 = QLabel(CAMDesigner)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 13, 6, 1, 1)

        self.lineEdit_2 = QLineEdit(CAMDesigner)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 6, 1, 1)

        self.label_21 = QLabel(CAMDesigner)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 19, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 21, 4, 1, 1)

        self.label_2 = QLabel(CAMDesigner)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_15 = QLabel(CAMDesigner)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 7, 6, 1, 1)

        self.lineEdit_9 = QLineEdit(CAMDesigner)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 18, 6, 1, 1)

        self.label_4 = QLabel(CAMDesigner)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.label_16 = QLabel(CAMDesigner)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 9, 6, 1, 1)

        self.label_7 = QLabel(CAMDesigner)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 13, 0, 1, 1)

        self.FallDegrees = QLineEdit(CAMDesigner)
        self.FallDegrees.setObjectName(u"FallDegrees")

        self.gridLayout.addWidget(self.FallDegrees, 12, 0, 1, 1)

        self.LowDwell = QLineEdit(CAMDesigner)
        self.LowDwell.setObjectName(u"LowDwell")

        self.gridLayout.addWidget(self.LowDwell, 14, 0, 1, 1)

        self.CAMPlot = QFrame(CAMDesigner)
        self.CAMPlot.setObjectName(u"CAMPlot")
        # Use Expanding policy instead of Fixed for resolution independence
        sizePolicy_plot = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy_plot.setHeightForWidth(self.CAMPlot.sizePolicy().hasHeightForWidth())
        self.CAMPlot.setSizePolicy(sizePolicy_plot)
        self.CAMPlot.setFrameShape(QFrame.Shape.StyledPanel)
        self.CAMPlot.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.CAMPlot, 1, 1, 20, 5)

        self.label_12 = QLabel(CAMDesigner)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 1, 6, 1, 1)

        self.lineEdit_5 = QLineEdit(CAMDesigner)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 10, 6, 1, 1)

        self.lineEdit_6 = QLineEdit(CAMDesigner)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 12, 6, 1, 1)

        self.lineEdit_7 = QLineEdit(CAMDesigner)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 14, 6, 1, 1)

        self.label_9 = QLabel(CAMDesigner)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 7)

        self.lineEdit_3 = QLineEdit(CAMDesigner)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lineEdit_3, 6, 6, 1, 1)

        self.lineEdit = QLineEdit(CAMDesigner)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 6, 1, 1)

        self.lineEdit_4 = QLineEdit(CAMDesigner)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 8, 6, 1, 1)

        self.label = QLabel(CAMDesigner)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_14 = QLabel(CAMDesigner)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 5, 6, 1, 1)

        self.label_13 = QLabel(CAMDesigner)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 3, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 21, 2, 1, 1)

        self.GraphBot = QPushButton(CAMDesigner)
        self.GraphBot.setObjectName(u"GraphBot")
        sizePolicy1.setHeightForWidth(self.GraphBot.sizePolicy().hasHeightForWidth())
        self.GraphBot.setSizePolicy(sizePolicy1)
        self.GraphBot.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.GraphBot, 21, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 21, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(734, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 22, 0, 1, 7)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(CAMDesigner)

        QMetaObject.connectSlotsByName(CAMDesigner)
    # setupUi

    def retranslateUi(self, CAMDesigner):
        CAMDesigner.setWindowTitle(QCoreApplication.translate("CAMDesigner", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("CAMDesigner", u"\nThickness (mm)", None))
        self.FallProfile.setItemText(0, QCoreApplication.translate("CAMDesigner", u"Linear", None))
        self.FallProfile.setItemText(1, QCoreApplication.translate("CAMDesigner", u"Parabolic", None))
        self.FallProfile.setItemText(2, QCoreApplication.translate("CAMDesigner", u"Harmonic", None))
        self.FallProfile.setItemText(3, QCoreApplication.translate("CAMDesigner", u"Cycloidal", None))

        self.label_11.setText(QCoreApplication.translate("CAMDesigner", u"\nFall Profile", None))
        self.label_8.setText(QCoreApplication.translate("CAMDesigner", u"\nNumber of Triangles", None))
        self.label_5.setText(QCoreApplication.translate("CAMDesigner", u"\nDegrees to Dwell", None))
        self.label_6.setText(QCoreApplication.translate("CAMDesigner", u"\nDegrees to Fall", None))
        self.RiseProfile.setItemText(0, QCoreApplication.translate("CAMDesigner", u"Linear", None))
        self.RiseProfile.setItemText(1, QCoreApplication.translate("CAMDesigner", u"Parabolic", None))
        self.RiseProfile.setItemText(2, QCoreApplication.translate("CAMDesigner", u"Harmonic", None))
        self.RiseProfile.setItemText(3, QCoreApplication.translate("CAMDesigner", u"Cycloidal", None))

        self.label_10.setText(QCoreApplication.translate("CAMDesigner", u"\nRise Profile", None))
        self.label_17.setText(QCoreApplication.translate("CAMDesigner", u"\nTextLabel", None))
        self.STEPBot.setText(QCoreApplication.translate("CAMDesigner", u"Generate STEP", None))
        self.CADBot.setText(QCoreApplication.translate("CAMDesigner", u"Generate CAD", None))
        self.label_19.setText(QCoreApplication.translate("CAMDesigner", u"\nTextLabel", None))
        self.label_20.setText(QCoreApplication.translate("CAMDesigner", u"\nTextLabel", None))
        self.label_18.setText(QCoreApplication.translate("CAMDesigner", u"\nTextLabel", None))
        self.label_21.setText(QCoreApplication.translate("CAMDesigner", u"\nTextLabel", None))
        self.label_2.setText(QCoreApplication.translate("CAMDesigner", u"\nTravel Radius (mm)", None))
        self.label_15.setText(QCoreApplication.translate("CAMDesigner", u"\nTextLabel", None))
        self.label_4.setText(QCoreApplication.translate("CAMDesigner", u"\nDegrees to Rise", None))
        self.label_16.setText(QCoreApplication.translate("CAMDesigner", u"\nTextLabel", None))
        self.label_7.setText(QCoreApplication.translate("CAMDesigner", u"\nDegrees to Dwell", None))
        self.label_12.setText(QCoreApplication.translate("CAMDesigner", u"\nTextLabel", None))
        self.label_9.setText(QCoreApplication.translate("CAMDesigner", u"CAM Designer", None))
        self.label.setText(QCoreApplication.translate("CAMDesigner", u"\nBase Radius (mm)", None))
        self.label_14.setText(QCoreApplication.translate("CAMDesigner", u"\nTextLabel", None))
        self.label_13.setText(QCoreApplication.translate("CAMDesigner", u"\nTextLabel", None))
        self.GraphBot.setText(QCoreApplication.translate("CAMDesigner", u"Generate Graph", None))
    # retranslateUi
