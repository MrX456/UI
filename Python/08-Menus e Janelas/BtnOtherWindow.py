# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BtnOtherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BtnOtherWindow(object):
    def setupUi(self, BtnOtherWindow):
        BtnOtherWindow.setObjectName("BtnOtherWindow")
        BtnOtherWindow.resize(349, 146)
        self.centralwidget = QtWidgets.QWidget(BtnOtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 70, 191, 21))
        self.label.setObjectName("label")
        BtnOtherWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(BtnOtherWindow)
        QtCore.QMetaObject.connectSlotsByName(BtnOtherWindow)

    def retranslateUi(self, BtnOtherWindow):
        _translate = QtCore.QCoreApplication.translate
        BtnOtherWindow.setWindowTitle(_translate("BtnOtherWindow", "Other Window"))
        self.label.setText(_translate("BtnOtherWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">Aqui temos uma outra janela</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BtnOtherWindow = QtWidgets.QMainWindow()
    ui = Ui_BtnOtherWindow()
    ui.setupUi(BtnOtherWindow)
    BtnOtherWindow.show()
    sys.exit(app.exec_())

