# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Table.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 241)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnPopulrTabela = QtWidgets.QPushButton(self.centralwidget)
        self.btnPopulrTabela.setGeometry(QtCore.QRect(260, 190, 101, 23))
        self.btnPopulrTabela.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPopulrTabela.setObjectName("btnPopulrTabela")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(170, 30, 321, 131))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnPopulrTabela.clicked.connect(self.popularTabela)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPopulrTabela.setText(_translate("MainWindow", "Popular Tabela"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "data_nasc"))

    def popularTabela(self):
        #Lista de pessoas
        pessoas = [{"id":"1", "nome":"João", "data_nasc":"01/02/1985"},
            {"id":"2", "nome":"Paulo", "data_nasc":"21/05/1991"},
            {"id":"3", "nome":"Pamella", "data_nasc":"12/07/1994"},
            {"id":"4", "nome":"Ana", "data_nasc":"30/01/1986"}]

        row = 0

        #A qtde de celulas deve ser do tamanho da lista de pessoas que vamos adicionar
        self.tableWidget.setRowCount(len(pessoas))

        #Vamos adicionar cada pessoa da lista na tabela
        for pessoa in pessoas:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(pessoa["id"]))#coluna indice 0
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(pessoa["nome"]))#coluna indice 1
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(pessoa["data_nasc"]))#coluna indice 2
            row += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

