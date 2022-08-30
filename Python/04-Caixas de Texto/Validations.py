# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Validations.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes

class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(752, 321)
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtTextoLivre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTextoLivre.setGeometry(QtCore.QRect(230, 50, 341, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtTextoLivre.setFont(font)
        self.txtTextoLivre.setObjectName("txtTextoLivre")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtInt = QtWidgets.QLineEdit(self.centralwidget)
        self.txtInt.setGeometry(QtCore.QRect(230, 110, 341, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtInt.setFont(font)
        self.txtInt.setObjectName("txtInt")
        self.txtFloat = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFloat.setGeometry(QtCore.QRect(230, 160, 341, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtFloat.setFont(font)
        self.txtFloat.setObjectName("txtFloat")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 160, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtCpf = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCpf.setGeometry(QtCore.QRect(230, 210, 341, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtCpf.setFont(font)
        self.txtCpf.setMaxLength(14)
        self.txtCpf.setObjectName("txtCpf")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 210, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtNulo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNulo.setGeometry(QtCore.QRect(230, 260, 341, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNulo.setFont(font)
        self.txtNulo.setReadOnly(True)
        self.txtNulo.setObjectName("txtNulo")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 260, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 290, 131, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        Janela.setCentralWidget(self.centralwidget)

        #Eventos de mudança de texto - Validar caracteres
        self.txtInt.textChanged.connect(self.isNumber)
        self.txtFloat.textChanged.connect(self.isFloat)

        #Evento do click
        self.pushButton.clicked.connect(self.validate)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Caixas de Texto"))
        self.label.setText(_translate("Janela", "Texto Livre"))
        self.label_2.setText(_translate("Janela", "Apenas Int"))
        self.label_3.setText(_translate("Janela", "Apenas Float"))
        self.txtCpf.setInputMask(_translate("Janela", "###.###.###-##"))
        self.label_4.setText(_translate("Janela", "Mascara CPF"))
        self.label_5.setText(_translate("Janela", "Nulo"))
        self.pushButton.setToolTip(_translate("Janela", "Enviar"))
        self.pushButton.setText(_translate("Janela", "Submit"))

    def isNumber(self):
        try:
            number = int(self.txtInt.text())
        except Exception:
            self.txtInt.setText("")

    def isFloat(self):
        try:
            #No Brasil usamos , ao inves de .
            number = float(self.txtFloat.text().replace(',','.'))
        except Exception:
            self.txtFloat.setText("")

    def validate(self):
        if self.txtNulo.text() == "":
            ctypes.windll.user32.MessageBoxW(0, "O campo está nulo", "Mensagem", 0)
        else:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela = QtWidgets.QMainWindow()
    ui = Ui_Janela()
    ui.setupUi(Janela)
    Janela.show()
    sys.exit(app.exec_())

