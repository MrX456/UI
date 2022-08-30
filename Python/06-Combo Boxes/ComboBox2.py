# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComboBox2.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 258)
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
        self.cboSexo = QtWidgets.QComboBox(self.centralwidget)
        self.cboSexo.setGeometry(QtCore.QRect(160, 90, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cboSexo.setFont(font)
        self.cboSexo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cboSexo.setEditable(False)
        self.cboSexo.setCurrentText("")
        self.cboSexo.setObjectName("cboSexo")
        self.btnSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubmit.setGeometry(QtCore.QRect(200, 200, 111, 23))
        self.btnSubmit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSubmit.setObjectName("btnSubmit")
        self.cboLinguagemFavorita = QtWidgets.QComboBox(self.centralwidget)
        self.cboLinguagemFavorita.setGeometry(QtCore.QRect(230, 130, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cboLinguagemFavorita.setFont(font)
        self.cboLinguagemFavorita.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cboLinguagemFavorita.setEditable(False)
        self.cboLinguagemFavorita.setCurrentText("")
        self.cboLinguagemFavorita.setObjectName("cboLinguagemFavorita")
        self.lblNome_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblNome_3.setGeometry(QtCore.QRect(50, 130, 171, 31))
        self.lblNome_3.setObjectName("lblNome_3")
        self.lblLinguagemFavorita = QtWidgets.QLabel(self.centralwidget)
        self.lblLinguagemFavorita.setGeometry(QtCore.QRect(160, 170, 181, 16))
        self.lblLinguagemFavorita.setText("")
        self.lblLinguagemFavorita.setObjectName("lblLinguagemFavorita")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cboSexo.setCurrentIndex(-1)
        self.cboLinguagemFavorita.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Adicionar itens na Combo Box
        self.cboSexo.addItem("Masculino")
        self.cboSexo.addItem("Feminino")

        #Podemos adicionar uma LISTA na combobox
        linguagens = ["Python", "Java", "Javascript", "C#", "PHP", "C++"]
        self.cboLinguagemFavorita.addItems(linguagens)

        #Deixar combo box clicavel
        self.cboLinguagemFavorita.activated.connect(self.mostrarLinguagemLabel)

        #Eventos de clique
        self.btnSubmit.clicked.connect(self.mostraDados)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ComboBox"))
        self.lblNome.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Nome:</span></p></body></html>"))
        self.lblNome_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Sexo:</span></p></body></html>"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit"))
        self.lblNome_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Linguagem Favorita:</span></p></body></html>"))

    def mostraDados(self):
        msg = QMessageBox()
        msg.setWindowTitle("Mensagem")
        msg.setText("Nome: " + self.txtNome.text() + "\n Sexo: " + self.cboSexo.currentText() + "\n Linguagem Favorita: " + self.cboLinguagemFavorita.currentText())
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def mostrarLinguagemLabel(self):
        self.lblLinguagemFavorita.setText(self.cboLinguagemFavorita.currentText())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

