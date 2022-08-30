# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Botoes.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes

class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(515, 205)
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.btnMudarTexto = QtWidgets.QPushButton(self.centralwidget)
        self.btnMudarTexto.setGeometry(QtCore.QRect(20, 150, 121, 23))
        self.btnMudarTexto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMudarTexto.setStyleSheet("color:blue")
        self.btnMudarTexto.setObjectName("btnMudarTexto")

        #Botao Mudar Texto
        self.btnMudarTexto.clicked.connect(self.mudarTexto)
        
        self.lblTexto = QtWidgets.QLabel(self.centralwidget)
        self.lblTexto.setGeometry(QtCore.QRect(20, 100, 121, 16))
        self.lblTexto.setObjectName("lblTexto")
        self.btnAbrirDialog = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbrirDialog.setGeometry(QtCore.QRect(200, 150, 121, 23))
        self.btnAbrirDialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAbrirDialog.setStyleSheet("background-color:green;\n"
"color:white")
        self.btnAbrirDialog.setObjectName("btnAbrirDialog")

        #Botao Abrir Dialog
        self.btnAbrirDialog.clicked.connect(self.abrirDialog)
        
        self.btnFechar = QtWidgets.QPushButton(self.centralwidget)
        self.btnFechar.setGeometry(QtCore.QRect(370, 150, 121, 23))
        self.btnFechar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFechar.setStyleSheet("background-color:red;\n"
"color:white")
        self.btnFechar.setObjectName("btnFechar")

        #Botao Fechar Aplicação
        self.btnFechar.clicked.connect(self.fecharApp)
        
        Janela.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Botoes"))
        self.btnMudarTexto.setText(_translate("Janela", "Mudar Texto"))
        self.lblTexto.setText(_translate("Janela", "<html><head/><body><p align=\"center\">Mensagem</p></body></html>"))
        self.btnAbrirDialog.setText(_translate("Janela", "Abrir Dialog"))
        self.btnFechar.setText(_translate("Janela", "Fechar Aplicação"))

    #Funções dos botões
    def mudarTexto(self):
        #Mudar texto da label
        self.lblTexto.setText("Olá Mundo")
        #Mudar propridades cor e deixar em negrito
        self.lblTexto.setStyleSheet("color:red;\n"
"font:bold")

    def abrirDialog(self):
        ctypes.windll.user32.MessageBoxW(0, "Você clicou no botão ABRIR DIALOG", "Mensagem", 0)

    def fecharApp(self):
        sys.exit(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela = QtWidgets.QMainWindow()
    ui = Ui_Janela()
    ui.setupUi(Janela)
    Janela.show()
    sys.exit(app.exec_())

