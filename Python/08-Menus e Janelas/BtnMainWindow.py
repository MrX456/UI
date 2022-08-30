# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BtnMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from BtnOtherWindow import Ui_BtnOtherWindow

class Ui_BtnMainWindow(object):
    def setupUi(self, BtnMainWindow):
        BtnMainWindow.setObjectName("BtnMainWindow")
        BtnMainWindow.resize(467, 170)
        self.centralwidget = QtWidgets.QWidget(BtnMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 90, 151, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 50, 221, 21))
        self.label.setObjectName("label")
        BtnMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(BtnMainWindow)
        QtCore.QMetaObject.connectSlotsByName(BtnMainWindow)

        #Evento de clique
        self.pushButton.clicked.connect(self.openWindow)

    def retranslateUi(self, BtnMainWindow):
        _translate = QtCore.QCoreApplication.translate
        BtnMainWindow.setWindowTitle(_translate("BtnMainWindow", "MainWindow"))
        self.pushButton.setText(_translate("BtnMainWindow", "Abrir janela"))
        self.label.setText(_translate("BtnMainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">Clique para abrir uma nova janela</span></p></body></html>"))

    #Abrir uma nova janela(A janela se chama BtnOtherWindow e sua classe já foi importada aqui)
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BtnOtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BtnMainWindow = QtWidgets.QMainWindow()
    ui = Ui_BtnMainWindow()
    ui.setupUi(BtnMainWindow)
    BtnMainWindow.show()
    sys.exit(app.exec_())

