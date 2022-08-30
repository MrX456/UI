# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmLoadingBackground.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time
from PyQt5.QtCore import QTimer
from FrmMain import Ui_MainWindow

class Ui_FrmLoading(object):
    def setupUi(self, FrmLoading):
        FrmLoading.setObjectName("FrmLoading")
        FrmLoading.resize(478, 257)
        FrmLoading.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        FrmLoading.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(FrmLoading)
        self.centralwidget.setObjectName("centralwidget")
        self.lblFundo = QtWidgets.QLabel(self.centralwidget)
        self.lblFundo.setGeometry(QtCore.QRect(0, 0, 491, 271))
        self.lblFundo.setText("")
        self.lblFundo.setPixmap(QtGui.QPixmap("splash_screen_backgroundA.png"))
        self.lblFundo.setObjectName("lblFundo")
        self.lblStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(60, 200, 101, 16))
        self.lblStatus.setObjectName("lblStatus")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(60, 220, 401, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        FrmLoading.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmLoading)
        QtCore.QMetaObject.connectSlotsByName(FrmLoading)

        #Precisamos de um timer para carregar a barra de progresso conforme avança
        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(25)

    def retranslateUi(self, FrmLoading):
        _translate = QtCore.QCoreApplication.translate
        self.lblStatus.setText(_translate("FrmLoading", "<html><head/><body><p><span style=\" color:#55ff00;\">Carregando...</span></p></body></html>"))

    #Esta função é responsável por aumentar valor da barra de progresso
    def loading(self):
        for i in range(100):
            time.sleep(0.1)
            self.progressBar.setValue(i)
            if i == 60:
                self.lblStatus.setText("Quase lá...")
                self.lblStatus.setStyleSheet("color:#55ff00;")
            #Quando o valor da barra chegar a 99 abrimos outra janela e paramos o timer
            if i == 99:
                self.timer.stop()
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.window)
                self.window.show()
                #Fechar esta tela
                FrmLoading.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmLoading = QtWidgets.QMainWindow()
    ui = Ui_FrmLoading()
    ui.setupUi(FrmLoading)

    #Remover bordas do formulario
    FrmLoading.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    FrmLoading.show()
    sys.exit(app.exec_())

