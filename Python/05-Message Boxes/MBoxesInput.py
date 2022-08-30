# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MBoxesInput.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox

class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(344, 129)
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.btnMessageC = QtWidgets.QPushButton(self.centralwidget)
        self.btnMessageC.setGeometry(QtCore.QRect(100, 60, 131, 21))
        self.btnMessageC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMessageC.setObjectName("btnMessageC")
        self.btnMessageD = QtWidgets.QPushButton(self.centralwidget)
        self.btnMessageD.setGeometry(QtCore.QRect(100, 100, 131, 21))
        self.btnMessageD.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMessageD.setObjectName("btnMessageD")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 121, 20))
        self.label.setObjectName("label")
        Janela.setCentralWidget(self.centralwidget)

        #Eventos de clique
        self.btnMessageC.clicked.connect(self.mboxInput)
        self.btnMessageD.clicked.connect(self.sair)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Message Boxes"))
        self.btnMessageC.setText(_translate("Janela", "Input"))
        self.btnMessageD.setText(_translate("Janela", "Sair"))
        self.label.setText(_translate("Janela", "Mensagem"))

    def mboxInput(self):
        inputBox = QInputDialog()

        #Titulo e Texto da Message Box
        inputBox.setWindowTitle("Nome")
        inputBox.setLabelText("Digite seu nome")

        #Mudar texto do botão ok e cancel
        inputBox.setOkButtonText("Confirmar")
        inputBox.setCancelButtonText("Cancelar")

        #Converter para inteiro
        x = int(inputBox.exec_())

        #Verificar se botão OK foi pressionado e campo não está vazio(Vale 1)
        if x == 1 and inputBox.textValue() != "":
            self.label.setText("Olá " + inputBox.textValue())

    def sair(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sair")
        msg.setText("Deseja encerrar aplicação?")
        msg.setIcon(QMessageBox.Question)

        #Botao com texto customizavel
        buttonoptionA = msg.addButton("Sim", QMessageBox.YesRole)
        buttonoptionB = msg.addButton("Não", QMessageBox.NoRole)

        x = msg.exec_()

        #Verificar se botão sim foi pressionado
        if msg.clickedButton() == buttonoptionA:
            sys.exit(0)
        elif msg.clickedButton() == buttonoptionB:
            print('Cancelado')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela = QtWidgets.QMainWindow()
    ui = Ui_Janela()
    ui.setupUi(Janela)
    Janela.show()
    sys.exit(app.exec_())

