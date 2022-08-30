# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextBoxes.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes

class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(720, 347)
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(150, 50, 51, 21))
        self.lblNome.setObjectName("lblNome")
        self.lblLogin = QtWidgets.QLabel(self.centralwidget)
        self.lblLogin.setGeometry(QtCore.QRect(150, 110, 51, 21))
        self.lblLogin.setObjectName("lblLogin")
        self.lblSenha = QtWidgets.QLabel(self.centralwidget)
        self.lblSenha.setGeometry(QtCore.QRect(150, 160, 51, 21))
        self.lblSenha.setObjectName("lblSenha")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(380, 230, 141, 31))
        self.btnCadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCadastrar.setStyleSheet("background-color:green;\n"
"color:white")
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.bntLimpar = QtWidgets.QPushButton(self.centralwidget)
        self.bntLimpar.setGeometry(QtCore.QRect(210, 230, 141, 31))
        self.bntLimpar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bntLimpar.setAcceptDrops(False)
        self.bntLimpar.setStyleSheet("background-color:red;\n"
"color:white")
        self.bntLimpar.setObjectName("bntLimpar")
        self.txtNome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNome.setGeometry(QtCore.QRect(200, 50, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNome.setFont(font)
        self.txtNome.setMaxLength(30)
        self.txtNome.setObjectName("txtNome")
        self.txtLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLogin.setGeometry(QtCore.QRect(200, 110, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtLogin.setFont(font)
        self.txtLogin.setMaxLength(15)
        self.txtLogin.setObjectName("txtLogin")
        self.txtSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSenha.setGeometry(QtCore.QRect(200, 160, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSenha.setFont(font)
        self.txtSenha.setInputMask("")
        self.txtSenha.setMaxLength(32767)
        self.txtSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtSenha.setObjectName("txtSenha")
        Janela.setCentralWidget(self.centralwidget)

        #Eventos de clique
        self.bntLimpar.clicked.connect(self.limparCampos)
        self.btnCadastrar.clicked.connect(self.mostrarDados)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Caixas de Texto"))
        self.lblNome.setText(_translate("Janela", "<html><head/><body><p><span style=\" font-size:12pt;\">Nome:</span></p></body></html>"))
        self.lblLogin.setText(_translate("Janela", "<html><head/><body><p><span style=\" font-size:12pt;\">Login:</span></p></body></html>"))
        self.lblSenha.setText(_translate("Janela", "<html><head/><body><p><span style=\" font-size:12pt;\">Senha:</span></p></body></html>"))
        self.btnCadastrar.setToolTip(_translate("Janela", "Cadastrar Dados"))
        self.btnCadastrar.setText(_translate("Janela", "Cadastrar"))
        self.bntLimpar.setToolTip(_translate("Janela", "Limpar Campos"))
        self.bntLimpar.setText(_translate("Janela", "Limpar"))
        self.txtNome.setToolTip(_translate("Janela", "Digite seu Nome"))
        self.txtNome.setPlaceholderText(_translate("Janela", "Digite seu Nome"))
        self.txtLogin.setToolTip(_translate("Janela", "Digite seu Login"))
        self.txtLogin.setPlaceholderText(_translate("Janela", "Digite seu Login"))
        self.txtSenha.setToolTip(_translate("Janela", "Digite sua Senha"))
        self.txtSenha.setPlaceholderText(_translate("Janela", "Digite sua Senha"))

    def limparCampos(self):
        #Mudar propriedade texto
        self.txtNome.setText("")
        self.txtLogin.setText("")
        self.txtSenha.setText("")

        #Focus
        self.txtNome.setFocus()

    def mostrarDados(self):
        nome = self.txtNome.text()
        login = self.txtLogin.text()
        senha = self.txtSenha.text()
        ctypes.windll.user32.MessageBoxW(0, "Seu nome é " + nome + "\n" + "Seu Login é " + login + "\nSua Senha é " +
                                            senha, "Dados do usuário", 0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela = QtWidgets.QMainWindow()
    ui = Ui_Janela()
    ui.setupUi(Janela)
    Janela.show()
    sys.exit(app.exec_())

