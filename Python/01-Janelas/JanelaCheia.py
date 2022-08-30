# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JanelaCheia.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(1280, 600)
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 270, 321, 111))
        self.label.setObjectName("label")
        Janela.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Full Screen"))
        self.label.setText(_translate("Janela", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Janela Cheia</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela = QtWidgets.QMainWindow()
    ui = Ui_Janela()
    ui.setupUi(Janela)

    #Mostrar maximizado
    Janela.showMaximized()

    sys.exit(app.exec_())

