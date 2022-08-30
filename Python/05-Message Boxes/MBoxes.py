# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MBoxes.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMessageBox


class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(344, 218)
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.btnMessageA = QtWidgets.QPushButton(self.centralwidget)
        self.btnMessageA.setGeometry(QtCore.QRect(100, 20, 131, 21))
        self.btnMessageA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMessageA.setObjectName("btnMessageA")
        self.btnMessageB = QtWidgets.QPushButton(self.centralwidget)
        self.btnMessageB.setGeometry(QtCore.QRect(100, 60, 131, 21))
        self.btnMessageB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMessageB.setObjectName("btnMessageB")
        self.btnMessageC = QtWidgets.QPushButton(self.centralwidget)
        self.btnMessageC.setGeometry(QtCore.QRect(100, 100, 131, 21))
        self.btnMessageC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMessageC.setObjectName("btnMessageC")
        self.btnMessageD = QtWidgets.QPushButton(self.centralwidget)
        self.btnMessageD.setGeometry(QtCore.QRect(100, 140, 131, 21))
        self.btnMessageD.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMessageD.setObjectName("btnMessageD")
        Janela.setCentralWidget(self.centralwidget)

        #Eventos de clique
        self.btnMessageA.clicked.connect(self.mensagemA)
        self.btnMessageB.clicked.connect(self.mensagemB)
        self.btnMessageC.clicked.connect(self.mensagemC)
        self.btnMessageD.clicked.connect(self.mensagemD)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Message Boxes"))
        self.btnMessageA.setText(_translate("Janela", "Mensagem1"))
        self.btnMessageB.setText(_translate("Janela", "Mensagem2"))
        self.btnMessageC.setText(_translate("Janela", "Mensagem3"))
        self.btnMessageD.setText(_translate("Janela", "Mensagem4"))

    def mensagemA(self):
        #Message Box simples com botão OK - Podemos editar varias propriedades como titulo, icone, texto...
        msg = QMessageBox()
        msg.setWindowTitle("Titulo da Message Box")
        msg.setText("Você está vendo uma Message Box simples!")
        x = msg.exec_()

    def mensagemB(self):
        #Message Box simples com botão OK e icone
        msg = QMessageBox()
        msg.setWindowTitle("Titulo da Message Box")
        msg.setText("Você está vendo uma Message Box simples com icone!")
        #Lista de icones
        #- QMessageBox.Critical
        #- QMessageBox.Warning
        #- QMessageBox.Information
        #- QMessageBox.Question
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    def mensagemC(self):
        #Message Box com tres botões
        msg = QMessageBox()
        msg.setWindowTitle("Titulo da Message Box")
        msg.setText("Você está vendo uma Message Box com tres botões!")
        msg.setIcon(QMessageBox.Information)
        #Lista de Buttons
        #- QMessageBox.Ok
        #- QMessageBox.Open
        #- QMessageBox.Save
        #- QMessageBox.Cancel
        #- QMessageBox.Yes
        #- QMessageBox.No
        #- QMessageBox.Abort
        #- QMessageBox.Retry
        #- QMessageBox.Ignore
        #Cada botão deve ser separado por |
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Ignore | QMessageBox.Cancel)
        x = msg.exec_()

    def mensagemD(self):
        #Message Box de SIM ou NAO
        msg = QMessageBox()
        msg.setWindowTitle("Message Box com duas opções")
        msg.setText("Você está vendo um Message Box com duas opções")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setIcon(QMessageBox.Question)
        msg.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela = QtWidgets.QMainWindow()
    ui = Ui_Janela()
    ui.setupUi(Janela)
    Janela.show()
    sys.exit(app.exec_())

