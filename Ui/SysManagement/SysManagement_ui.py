# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SysManagement.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QToolButton, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1246, 783)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 85, 127, 179))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(0, 128, 190, 179))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(0, 106, 158, 179))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(0, 43, 63, 179))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(0, 57, 85, 179))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(0, 42, 63, 217))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush9 = QBrush(QColor(255, 255, 255, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush10 = QBrush(QColor(0, 43, 63, 89))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        brush11 = QBrush(QColor(0, 60, 89, 179))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush11)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Run = QToolButton(self.centralwidget)
        self.Run.setObjectName(u"Run")
        self.Run.setGeometry(QRect(30, 20, 171, 161))
        self.Run.setStyleSheet(u"font: 700 18pt \"Microsoft YaHei UI\";")
        icon = QIcon()
        icon.addFile(u":/img/Icon/Run.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Run.setIcon(icon)
        self.Run.setIconSize(QSize(120, 120))
        self.Run.setCheckable(False)
        self.Run.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.Run.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.Edit = QToolButton(self.centralwidget)
        self.Edit.setObjectName(u"Edit")
        self.Edit.setGeometry(QRect(230, 20, 171, 161))
        self.Edit.setStyleSheet(u"font: 700 18pt \"Microsoft YaHei UI\";\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/img/Icon/Edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Edit.setIcon(icon1)
        self.Edit.setIconSize(QSize(120, 120))
        self.Edit.setCheckable(False)
        self.Edit.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.Edit.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.Set = QToolButton(self.centralwidget)
        self.Set.setObjectName(u"Set")
        self.Set.setGeometry(QRect(420, 20, 171, 161))
        self.Set.setStyleSheet(u"font: 700 18pt \"Microsoft YaHei UI\";\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/img/Icon/Set.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Set.setIcon(icon2)
        self.Set.setIconSize(QSize(120, 120))
        self.Set.setCheckable(False)
        self.Set.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.Set.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.Exit = QToolButton(self.centralwidget)
        self.Exit.setObjectName(u"Exit")
        self.Exit.setGeometry(QRect(620, 20, 171, 161))
        self.Exit.setStyleSheet(u"font: 700 18pt \"Microsoft YaHei UI\";\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/img/Icon/Exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Exit.setIcon(icon3)
        self.Exit.setIconSize(QSize(120, 120))
        self.Exit.setCheckable(False)
        self.Exit.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.Exit.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1246, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Run.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u6d4b\u8bd5", None))
        self.Edit.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u6d4b\u8bd5", None))
        self.Set.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.Exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7cfb\u7edf", None))
    # retranslateUi

