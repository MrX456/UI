# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MBoxes2.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMessageBox
from PyQt5.QtGui import QPixmap

class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(344, 129)
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.btnMessageA = QtWidgets.QPushButton(self.centralwidget)
        self.btnMessageA.setGeometry(QtCore.QRect(100, 20, 131, 21))
        self.btnMessageA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMessageA.setObjectName("btnMessageA")
        self.btnMessageC = QtWidgets.QPushButton(self.centralwidget)
        self.btnMessageC.setGeometry(QtCore.QRect(100, 60, 131, 21))
        self.btnMessageC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMessageC.setObjectName("btnMessageC")
        self.btnMessageD = QtWidgets.QPushButton(self.centralwidget)
        self.btnMessageD.setGeometry(QtCore.QRect(100, 100, 131, 21))
        self.btnMessageD.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMessageD.setObjectName("btnMessageD")
        Janela.setCentralWidget(self.centralwidget)

        #Eventos de clique
        self.btnMessageA.clicked.connect(self.mensagem)
        self.btnMessageC.clicked.connect(self.status)
        self.btnMessageD.clicked.connect(self.sair)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Message Boxes"))
        self.btnMessageA.setText(_translate("Janela", "Mensagem"))
        self.btnMessageC.setText(_translate("Janela", "Status"))
        self.btnMessageD.setText(_translate("Janela", "Sair"))

    def mensagem(self):
        #Message Box simples com botão OK e icone
        msg = QMessageBox()
        msg.setWindowTitle("Mensagem")
        msg.setText("Mensagem exibida com sucesso!")

        #Icone customizado por caminho relativo
        msg.setIconPixmap(QPixmap("chat-4-64.png"))
        x = msg.exec_()


    def status(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message Box com Detalhes")
        msg.setText("Aqui temos uma Message Box com detalhes!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        #Message Box com detalhes
        msg.setDetailedText("Aqui podemos inserir um texto que será exibido se clicar no botão show details.")
        x = msg.exec_()

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

