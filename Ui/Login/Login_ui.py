# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1001, 708)
        Form.setMinimumSize(QSize(600, 0))
        Form.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.188889 rgba(255, 179, 228, 255), stop:1 rgba(255, 255, 255, 255));")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(391, 471))
        self.groupBox.setMaximumSize(QSize(391, 471))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"QGroupBox\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:transparent;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.177778 rgba(255, 131, 223, 243), stop:1 rgba(255, 255, 255, 255));\n"
"border:transparent;\n"
"}\n"
"QLineEdit\n"
"{\n"
"	border-top:transparent;\n"
"    border-left:transparent;\n"
"    border-right:transparent;\n"
"    border-bottom:1px solid black;\n"
"    background: transparent;\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"	color: rgb(136, 136, 136);\n"
"}\n"
"QComboBox\n"
"{\n"
"	border-top:transparent;\n"
"    border-left:transparent;\n"
"    border-right:transparent;\n"
"    border-bottom:1px solid black;\n"
"    background: transparent;\n"
"    font: 12pt \"Microsoft YaHei UI\";\n"
"    color: rgb(136, 136, 136);\n"
"}\n"
"QLable\n"
"{\n"
" background: transparent;\n"
" align: center;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    outline: 0px solid gray;   /* \u9009\u5b9a\u9879\u7684\u865a"
                        "\u6846 */\n"
"    border: 1px solid yellow;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"	color: rgb(97, 97, 97);\n"
"	background-color: rgb(255, 255, 255);\n"
"    selection-background-color: lightgreen;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u4e2d\u9879\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    height: 50px;   /* \u9879\u7684\u9ad8\u5ea6\uff08\u8bbe\u7f6epComboBox->setView(new QListView());\u540e\uff0c\u8be5\u9879\u624d\u8d77\u4f5c\u7528\uff09 */\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 5, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 7, 2, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(300, 40))

        self.gridLayout.addWidget(self.pushButton, 5, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(280, 40))

        self.verticalLayout.addWidget(self.comboBox)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(280, 40))
        self.lineEdit_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.lineEdit_2)


        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setUnderline(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"username", None))

        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"password", None))
        self.label.setText(QCoreApplication.translate("Form", u"     Login", None))
    # retranslateUi

