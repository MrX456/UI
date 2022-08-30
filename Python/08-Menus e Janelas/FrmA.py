# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmA.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FrmA(object):
    def setupUi(self, FrmA):
        FrmA.setObjectName("FrmA")
        FrmA.resize(397, 149)
        self.centralwidget = QtWidgets.QWidget(FrmA)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 60, 141, 31))
        self.label.setObjectName("label")
        FrmA.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmA)
        QtCore.QMetaObject.connectSlotsByName(FrmA)

    def retranslateUi(self, FrmA):
        _translate = QtCore.QCoreApplication.translate
        FrmA.setWindowTitle(_translate("FrmA", "Form A"))
        self.label.setText(_translate("FrmA", "<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">Este é o formulario A</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmA = QtWidgets.QMainWindow()
    ui = Ui_FrmA()
    ui.setupUi(FrmA)
    FrmA.show()
    sys.exit(app.exec_())

