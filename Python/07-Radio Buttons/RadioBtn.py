# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RadioBtn.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(302, 201)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblLiguagenFavorita = QtWidgets.QLabel(self.centralwidget)
        self.lblLiguagenFavorita.setGeometry(QtCore.QRect(80, 160, 161, 21))
        self.lblLiguagenFavorita.setObjectName("lblLiguagenFavorita")
        self.radPython = QtWidgets.QRadioButton(self.centralwidget)
        self.radPython.setGeometry(QtCore.QRect(100, 20, 82, 17))
        self.radPython.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radPython.setObjectName("radPython")
        self.radJava = QtWidgets.QRadioButton(self.centralwidget)
        self.radJava.setGeometry(QtCore.QRect(100, 50, 82, 17))
        self.radJava.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radJava.setObjectName("radJava")
        self.radPHP = QtWidgets.QRadioButton(self.centralwidget)
        self.radPHP.setGeometry(QtCore.QRect(100, 80, 82, 17))
        self.radPHP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radPHP.setObjectName("radPHP")
        self.radJavascript = QtWidgets.QRadioButton(self.centralwidget)
        self.radJavascript.setGeometry(QtCore.QRect(100, 110, 82, 17))
        self.radJavascript.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radJavascript.setObjectName("radJavascript")
        self.btnSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubmit.setGeometry(QtCore.QRect(110, 130, 75, 23))
        self.btnSubmit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSubmit.setObjectName("btnSubmit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Eventos de clique
        self.btnSubmit.clicked.connect(self.mostraLinguagemFavorita)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Radio Buttons"))
        self.lblLiguagenFavorita.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Escolha sua linguagem</span></p></body></html>"))
        self.radPython.setText(_translate("MainWindow", "Python"))
        self.radJava.setText(_translate("MainWindow", "Java"))
        self.radPHP.setText(_translate("MainWindow", "PHP"))
        self.radJavascript.setText(_translate("MainWindow", "Javascript"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit"))

    def mostraLinguagemFavorita(self):
        #Verificar qual Radio Button está selecionado
        if self.radPython.isChecked():
            self.lblLiguagenFavorita.setText(self.radPython.text())

        elif self.radJava.isChecked():
            self.lblLiguagenFavorita.setText(self.radJava.text())

        elif self.radPHP.isChecked():
            self.lblLiguagenFavorita.setText(self.radPHP.text())

        elif self.radJavascript.isChecked():
            self.lblLiguagenFavorita.setText(self.radJavascript.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

