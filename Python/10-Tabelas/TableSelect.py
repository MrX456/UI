# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableSelect.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 246)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 30, 261, 171))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.txtA = QtWidgets.QLineEdit(self.centralwidget)
        self.txtA.setGeometry(QtCore.QRect(340, 60, 191, 20))
        self.txtA.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtA.setReadOnly(True)
        self.txtA.setObjectName("txtA")
        self.txtB = QtWidgets.QLineEdit(self.centralwidget)
        self.txtB.setGeometry(QtCore.QRect(340, 100, 191, 20))
        self.txtB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtB.setReadOnly(True)
        self.txtB.setObjectName("txtB")
        self.txtC = QtWidgets.QLineEdit(self.centralwidget)
        self.txtC.setGeometry(QtCore.QRect(340, 140, 191, 20))
        self.txtC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtC.setReadOnly(True)
        self.txtC.setObjectName("txtC")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Largura de cada coluna
        self.tableWidget.setColumnWidth(0, 40)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 80)

        self.popularTabela()

        #Este código é necessario para selecionar uma linha inteira ao invés de uma celula individual
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        #Evento de seleção de uma linha da tabela
        self.tableWidget.itemSelectionChanged.connect(self.setCampos)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Selecionar Linha"))
        self.tableWidget.setToolTip(_translate("MainWindow", "Clique sobre a linha desejada para selecionar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "item"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "qtde"))

    def popularTabela(self):
        #Lista de produtos
        produtos = [{"id":"1", "item":"Caneta Azul", "qtde":"80"},
            {"id":"2", "item":"Lapiseira 0.7", "qtde":"30"},
            {"id":"3", "item":"Borracha Branca", "qtde":"100"},
            {"id":"4", "item":"Apontador", "qtde":"40"}]

        row = 0

        #A qtde de celulas deve ser do tamanho da lista de pessoas que vamos adicionar
        self.tableWidget.setRowCount(len(produtos))

        #Vamos adicionar cada produto da lista na tabela
        for produto in produtos:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(produto["id"]))#coluna indice 0
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(produto["item"]))#coluna indice 1
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(produto["qtde"]))#coluna indice 2
            row += 1

    def setCampos(self):
        try:
            items = self.tableWidget.selectedItems()
            self.txtA.setText(str(items[0].text()))
            self.txtB.setText(str(items[1].text()))
            self.txtC.setText(str(items[2].text()))

        except Exception as e:
            print("Voce clicou fora da area da tabela! -> " + str(e))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

