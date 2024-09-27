from PySide6.QtWidgets import QMainWindow,QApplication,QDialog
from PySide6 import QtCore
from PySide6.QtCore import QTranslator
import sys
from Ui.SysManagement.SysManagement_ui import SysManagement
from Ui.Login.Login_ui import Login
from PySide6.QtWidgets import QMessageBox

class SysManagementWindow(QMainWindow, SysManagement):
    jurisdiction=0
    def __init__(self):
        super(SysManagementWindow,self).__init__()
        self.setupUi(self)
        self.showMaximized()#max show
        self.Exit.clicked.connect(self.close)#exit ui

    def jur_if(self):
        print(self.jurisdiction)
        if self.jurisdiction<=1:#jurisdiction 1
            print("jurisdiction")
            self.Run.setDisabled(False)
            self.Edit.setDisabled(True)
            self.Set.setDisabled(True)
            pass
        elif self.jurisdiction==2:
            self.Run.setDisabled(False)
            self.Edit.setDisabled(False)
            self.Set.setDisabled(False)
            pass

class Login_UI(QDialog, Login):
    jurisdiction=0
    def __init__(self):
        super(Login_UI,self).__init__()
        self.setupUi(self)
        self.setModal(True)
        self.jurisdiction=2
        self.translator = QTranslator()
        self.translator.load("./Ui/login/Login.qm")
        _app = QApplication.instance()
        _app.installTranslator(self.translator)
        self.retranslateUi(self)
	
        self.groupBox.move((self.size().width()-self.groupBox.size().width())/2,(self.size().height()-self.groupBox.size().height())/2)
        self.showMaximized()#max show
    def resizeEvent(self, evt):
        #info = 'w = {0}; h = {1}'.format(evt.size().width(),evt.size().height())
        self.groupBox.move((evt.size().width()-self.groupBox.size().width())/2,(evt.size().height()-self.groupBox.size().height())/2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Logui=Login_UI()
    Logui.exec_()
    SysMag = SysManagementWindow()
    SysMag.jurisdiction=Logui.jurisdiction
    SysMag.jur_if()
    SysMag.show()
    sys.exit(app.exec_())

