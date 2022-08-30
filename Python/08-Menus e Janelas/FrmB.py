# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmB.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FrmB(object):
    def setupUi(self, FrmB):
        FrmB.setObjectName("FrmB")
        FrmB.resize(399, 149)
        self.centralwidget = QtWidgets.QWidget(FrmB)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 60, 141, 31))
        self.label_2.setObjectName("label_2")
        FrmB.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmB)
        QtCore.QMetaObject.connectSlotsByName(FrmB)

    def retranslateUi(self, FrmB):
        _translate = QtCore.QCoreApplication.translate
        FrmB.setWindowTitle(_translate("FrmB", "Form B"))
        self.label_2.setText(_translate("FrmB", "<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">Este é o formulario B</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmB = QtWidgets.QMainWindow()
    ui = Ui_FrmB()
    ui.setupUi(FrmB)
    FrmB.show()
    sys.exit(app.exec_())

