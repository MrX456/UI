# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableCars.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 289)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 321, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.lblModelo = QtWidgets.QLabel(self.centralwidget)
        self.lblModelo.setGeometry(QtCore.QRect(350, 80, 47, 13))
        self.lblModelo.setObjectName("lblModelo")
        self.txtModelo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtModelo.setGeometry(QtCore.QRect(410, 80, 211, 20))
        self.txtModelo.setObjectName("txtModelo")
        self.txtCor = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCor.setGeometry(QtCore.QRect(410, 110, 211, 20))
        self.txtCor.setObjectName("txtCor")
        self.lblCor = QtWidgets.QLabel(self.centralwidget)
        self.lblCor.setGeometry(QtCore.QRect(350, 110, 47, 13))
        self.lblCor.setObjectName("lblCor")
        self.txtPreco = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPreco.setGeometry(QtCore.QRect(410, 140, 211, 20))
        self.txtPreco.setObjectName("txtPreco")
        self.lblPreco = QtWidgets.QLabel(self.centralwidget)
        self.lblPreco.setGeometry(QtCore.QRect(350, 140, 47, 13))
        self.lblPreco.setObjectName("lblPreco")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(470, 50, 41, 16))
        self.lblTitle.setObjectName("lblTitle")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(420, 170, 161, 23))
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd.setObjectName("btnAdd")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(420, 200, 161, 23))
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSave.setObjectName("btnSave")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Largura de cada colunas
        self.tableWidget.setColumnWidth(0, 110)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 80)

        self.btnAdd.clicked.connect(self.addCarro)
        self.btnSave.clicked.connect(self.saveCarro)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Adicionar Carros Tabela"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Modelo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cor"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Preço"))
        self.lblModelo.setText(_translate("MainWindow", "Modelo :"))
        self.lblCor.setText(_translate("MainWindow", "Cor:"))
        self.lblPreco.setText(_translate("MainWindow", "Preço:"))
        self.lblTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Carro</span></p></body></html>"))
        self.btnAdd.setToolTip(_translate("MainWindow", "Adiconar carro na tabela"))
        self.btnAdd.setText(_translate("MainWindow", "Adicionar"))
        self.btnSave.setToolTip(_translate("MainWindow", "Guardas dados em txt"))
        self.btnSave.setText(_translate("MainWindow", "Guardar Dados"))

    def addCarro(self):
        if self.txtModelo.text() != "" and self.txtCor.text() != "" and self.txtPreco.text() != "":
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)

            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(self.txtModelo.text()))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(self.txtCor.text()))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(self.txtPreco.text()))

            self.txtModelo.setText("")
            self.txtCor.setText("")
            self.txtPreco.setText("")

        else:
            #Message Box simples com botão OK e icone
            msg = QMessageBox()
            msg.setWindowTitle("Mensagem")
            msg.setText("Preencha todos os campos para adicionar!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def saveCarro(self):
        if self.tableWidget.rowCount() != 0:
            file = open("saved_cars.txt", "w+")

            for row in range(self.tableWidget.rowCount()):
                file.write(self.tableWidget.item(row, 0).text() + " - ")
                file.write(self.tableWidget.item(row, 1).text() + " - $")
                file.write(self.tableWidget.item(row, 2).text() + "\n")

            file.close()

            #abrir arquivo
            path = "saved_cars.txt"
            os.system(path)

        else:
            #Message Box simples com botão OK e icone
            msg = QMessageBox()
            msg.setWindowTitle("Mensagem")
            msg.setText("Não há dados na tabela para salvar!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

