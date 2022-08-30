# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextFields.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes

class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(502, 310)
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(50, 40, 51, 21))
        self.lblNome.setObjectName("lblNome")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(280, 220, 141, 31))
        self.btnCadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCadastrar.setStyleSheet("background-color:green;\n"
"color:white")
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.bntLimpar = QtWidgets.QPushButton(self.centralwidget)
        self.bntLimpar.setGeometry(QtCore.QRect(110, 220, 141, 31))
        self.bntLimpar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bntLimpar.setAcceptDrops(False)
        self.bntLimpar.setStyleSheet("background-color:red;\n"
"color:white")
        self.bntLimpar.setObjectName("bntLimpar")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 40, 301, 161))
        self.textEdit.setObjectName("textEdit")
        Janela.setCentralWidget(self.centralwidget)

        #Eventos de clique
        self.bntLimpar.clicked.connect(self.limparCampos)
        self.btnCadastrar.clicked.connect(self.guardarTexto)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Caixas de Texto"))
        self.lblNome.setText(_translate("Janela", "<html><head/><body><p><span style=\" font-size:12pt;\">Nome:</span></p></body></html>"))
        self.btnCadastrar.setToolTip(_translate("Janela", "Cadastrar Dados"))
        self.btnCadastrar.setText(_translate("Janela", "Guardar Texto"))
        self.bntLimpar.setToolTip(_translate("Janela", "Limpar Campos"))
        self.bntLimpar.setText(_translate("Janela", "Limpar"))

    def limparCampos(self):
        #Limpar Text Edit
        self.textEdit.setPlainText("")

    def guardarTexto(self):
        try:
            arquivo = open("texto_guardado.txt","+w")

            #Vamos pegar o texto do campo e escrever no txt
            arquivo.write(self.textEdit.toPlainText())
            arquivo.close()
            ctypes.windll.user32.MessageBoxW(0, "Arquivo criado com sucesso", "OK", 0)

        except:
            ctypes.windll.user32.MessageBoxW(0, "Não foi possivel criar o arquivo", "Erro", 0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela = QtWidgets.QMainWindow()
    ui = Ui_Janela()
    ui.setupUi(Janela)
    Janela.show()
    sys.exit(app.exec_())

