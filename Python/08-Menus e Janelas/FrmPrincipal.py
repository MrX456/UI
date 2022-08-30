# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from FrmA import Ui_FrmA
from FrmB import Ui_FrmB
from PyQt5.QtWidgets import QMessageBox, QMessageBox

class Ui_FrmPrincipal(object):
    def setupUi(self, FrmPrincipal):
        FrmPrincipal.setObjectName("FrmPrincipal")
        FrmPrincipal.resize(461, 245)
        self.centralwidget = QtWidgets.QWidget(FrmPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        FrmPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrmPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 21))
        self.menubar.setObjectName("menubar")
        self.menuJanelas = QtWidgets.QMenu(self.menubar)
        self.menuJanelas.setObjectName("menuJanelas")
        self.menuOp_es = QtWidgets.QMenu(self.menubar)
        self.menuOp_es.setObjectName("menuOp_es")
        FrmPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrmPrincipal)
        self.statusbar.setObjectName("statusbar")
        FrmPrincipal.setStatusBar(self.statusbar)
        self.actionSair = QtWidgets.QAction(FrmPrincipal)
        self.actionSair.setObjectName("actionSair")
        self.actionA = QtWidgets.QAction(FrmPrincipal)
        self.actionA.setObjectName("actionA")
        self.actionB = QtWidgets.QAction(FrmPrincipal)
        self.actionB.setObjectName("actionB")
        self.menuJanelas.addAction(self.actionA)
        self.menuJanelas.addAction(self.actionB)
        self.menuOp_es.addAction(self.actionSair)
        self.menubar.addAction(self.menuJanelas.menuAction())
        self.menubar.addAction(self.menuOp_es.menuAction())

        self.retranslateUi(FrmPrincipal)
        QtCore.QMetaObject.connectSlotsByName(FrmPrincipal)

        #Eventos dos itens do menu
        self.actionA.triggered.connect(self.abrirFormA)
        self.actionB.triggered.connect(self.abrirFormB)
        self.actionSair.triggered.connect(self.sair)

    def retranslateUi(self, FrmPrincipal):
        _translate = QtCore.QCoreApplication.translate
        FrmPrincipal.setWindowTitle(_translate("FrmPrincipal", "Janela Principal"))
        self.menuJanelas.setTitle(_translate("FrmPrincipal", "Janelas"))
        self.menuOp_es.setTitle(_translate("FrmPrincipal", "Opções"))
        self.actionSair.setText(_translate("FrmPrincipal", "Sair"))
        self.actionA.setText(_translate("FrmPrincipal", "A"))
        self.actionB.setText(_translate("FrmPrincipal", "B"))

    def abrirFormA(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FrmA()
        self.ui.setupUi(self.window)
        self.window.show()

    def abrirFormB(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FrmB()
        self.ui.setupUi(self.window)
        self.window.show()

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
    FrmPrincipal = QtWidgets.QMainWindow()
    ui = Ui_FrmPrincipal()
    ui.setupUi(FrmPrincipal)
    FrmPrincipal.show()
    sys.exit(app.exec_())

