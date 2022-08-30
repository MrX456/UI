# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Botao.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 163)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 130, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")

        #Aqui temos o evento de clique no botao que vai executar a função buttonClicked
        self.pushButton.clicked.connect(self.clickButton)
        
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 60, 401, 41))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setToolTip(_translate("Dialog", "Clique para ver a mensagem"))
        self.pushButton.setText(_translate("Dialog", "Clique"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Mensagem</span></p></body></html>"))

     # action method
    def clickButton(self):
  
        # button pressed - exibir um dialog qualquer
        #ctypes.windll.user32.MessageBoxW(0, "Você apertou o botão", "Mensagem", 1) DIALOG COM DOIS BOTÕES
        ctypes.windll.user32.MessageBoxW(0, "Você apertou o botão", "Mensagem", 0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

