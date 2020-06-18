# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ass4Q1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(360, 230)
        self.sportInput = QtGui.QLineEdit(Dialog)
        self.sportInput.setGeometry(QtCore.QRect(140, 40, 161, 20))
        self.sportInput.setObjectName(_fromUtf8("sportInput"))
        self.characterInput = QtGui.QLineEdit(Dialog)
        self.characterInput.setGeometry(QtCore.QRect(140, 70, 41, 20))
        self.characterInput.setObjectName(_fromUtf8("characterInput"))
        self.countButton = QtGui.QPushButton(Dialog)
        self.countButton.setGeometry(QtCore.QRect(140, 120, 75, 23))
        self.countButton.setObjectName(_fromUtf8("countButton"))
        self.sportLabel = QtGui.QLabel(Dialog)
        self.sportLabel.setGeometry(QtCore.QRect(30, 40, 101, 16))
        self.sportLabel.setObjectName(_fromUtf8("sportLabel"))
        self.characterLabel = QtGui.QLabel(Dialog)
        self.characterLabel.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.characterLabel.setObjectName(_fromUtf8("characterLabel"))
        self.Title = QtGui.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(110, 10, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName(_fromUtf8("Title"))
        self.displayLabel = QtGui.QLabel(Dialog)
        self.displayLabel.setGeometry(QtCore.QRect(30, 172, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.displayLabel.setFont(font)
        self.displayLabel.setText(_fromUtf8(""))
        self.displayLabel.setObjectName(_fromUtf8("displayLabel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.countButton.setText(_translate("Dialog", "Count", None))
        self.sportLabel.setText(_translate("Dialog", "Enter Olympic Sport", None))
        self.characterLabel.setText(_translate("Dialog", "Enter Character", None))
        self.Title.setText(_translate("Dialog", "Olympic Sport Character Count", None))

