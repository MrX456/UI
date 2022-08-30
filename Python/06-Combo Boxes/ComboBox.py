# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComboBox.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 175)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(100, 40, 61, 31))
        self.lblNome.setObjectName("lblNome")
        self.txtNome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNome.setGeometry(QtCore.QRect(160, 49, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNome.setFont(font)
        self.txtNome.setObjectName("txtNome")
        self.lblNome_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblNome_2.setGeometry(QtCore.QRect(100, 90, 51, 31))
        self.lblNome_2.setObjectName("lblNome_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 90, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.btnSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubmit.setGeometry(QtCore.QRect(190, 140, 111, 23))
        self.btnSubmit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSubmit.setObjectName("btnSubmit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Adicionar itens na Combo Box
        self.comboBox.addItem("Masculino")
        self.comboBox.addItem("Feminino")

        #Eventos de clique
        self.btnSubmit.clicked.connect(self.mostraDados)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblNome.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Nome:</span></p></body></html>"))
        self.lblNome_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Sexo:</span></p></body></html>"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit"))

    def mostraDados(self):
        msg = QMessageBox()
        msg.setWindowTitle("Mensagem")
        msg.setText("Nome: " + self.txtNome.text() + "\n Sexo: " + self.comboBox.currentText())
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

