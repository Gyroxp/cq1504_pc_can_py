# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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

class Ui_dlgMain(object):
    def setupUi(self, dlgMain):
        dlgMain.setObjectName(_fromUtf8("dlgMain"))
        dlgMain.resize(800, 480)
        self.lineEdit_IP = QtGui.QLineEdit(dlgMain)
        self.lineEdit_IP.setGeometry(QtCore.QRect(50, 12, 133, 20))
        self.lineEdit_IP.setText(_fromUtf8(""))
        self.lineEdit_IP.setObjectName(_fromUtf8("lineEdit_IP"))
        self.label = QtGui.QLabel(dlgMain)
        self.label.setGeometry(QtCore.QRect(10, 12, 30, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(dlgMain)
        self.frame.setGeometry(QtCore.QRect(0, 0, 201, 71))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 31, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_port = QtGui.QLineEdit(self.frame)
        self.lineEdit_port.setGeometry(QtCore.QRect(51, 42, 41, 20))
        self.lineEdit_port.setText(_fromUtf8(""))
        self.lineEdit_port.setObjectName(_fromUtf8("lineEdit_port"))
        self.pushBtn_connect = QtGui.QPushButton(self.frame)
        self.pushBtn_connect.setGeometry(QtCore.QRect(110, 40, 75, 23))
        self.pushBtn_connect.setObjectName(_fromUtf8("pushBtn_connect"))
        self.label_3 = QtGui.QLabel(dlgMain)
        self.label_3.setGeometry(QtCore.QRect(411, 11, 48, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(dlgMain)
        self.label_4.setGeometry(QtCore.QRect(604, 11, 36, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_GPID = QtGui.QLineEdit(dlgMain)
        self.lineEdit_GPID.setGeometry(QtCore.QRect(646, 11, 133, 20))
        self.lineEdit_GPID.setObjectName(_fromUtf8("lineEdit_GPID"))
        self.textEdit_status = QtGui.QTextEdit(dlgMain)
        self.textEdit_status.setGeometry(QtCore.QRect(0, 390, 801, 91))
        self.textEdit_status.setObjectName(_fromUtf8("textEdit_status"))
        self.pushBtn_PreSwOff = QtGui.QPushButton(dlgMain)
        self.pushBtn_PreSwOff.setGeometry(QtCore.QRect(467, 41, 75, 23))
        self.pushBtn_PreSwOff.setObjectName(_fromUtf8("pushBtn_PreSwOff"))
        self.pushBtn_ExecSwOff = QtGui.QPushButton(dlgMain)
        self.pushBtn_ExecSwOff.setGeometry(QtCore.QRect(548, 41, 75, 23))
        self.pushBtn_ExecSwOff.setObjectName(_fromUtf8("pushBtn_ExecSwOff"))
        self.pushBtn_PreSwOn = QtGui.QPushButton(dlgMain)
        self.pushBtn_PreSwOn.setGeometry(QtCore.QRect(629, 41, 75, 23))
        self.pushBtn_PreSwOn.setObjectName(_fromUtf8("pushBtn_PreSwOn"))
        self.pushBtn_ExecSwOn = QtGui.QPushButton(dlgMain)
        self.pushBtn_ExecSwOn.setGeometry(QtCore.QRect(710, 41, 75, 23))
        self.pushBtn_ExecSwOn.setObjectName(_fromUtf8("pushBtn_ExecSwOn"))
        self.layoutWidget = QtGui.QWidget(dlgMain)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_TCID = QtGui.QLineEdit(dlgMain)
        self.lineEdit_TCID.setGeometry(QtCore.QRect(465, 11, 133, 20))
        self.lineEdit_TCID.setObjectName(_fromUtf8("lineEdit_TCID"))
        self.pushBtn_getRealData = QtGui.QPushButton(dlgMain)
        self.pushBtn_getRealData.setGeometry(QtCore.QRect(386, 41, 75, 23))
        self.pushBtn_getRealData.setObjectName(_fromUtf8("pushBtn_getRealData"))
        self.pushBtn_clrStatus = QtGui.QPushButton(dlgMain)
        self.pushBtn_clrStatus.setGeometry(QtCore.QRect(720, 360, 75, 23))
        self.pushBtn_clrStatus.setObjectName(_fromUtf8("pushBtn_clrStatus"))
        self.layoutWidget.raise_()
        self.frame.raise_()
        self.lineEdit_IP.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit_GPID.raise_()
        self.lineEdit_TCID.raise_()
        self.textEdit_status.raise_()
        self.pushBtn_PreSwOff.raise_()
        self.pushBtn_ExecSwOff.raise_()
        self.pushBtn_PreSwOn.raise_()
        self.pushBtn_ExecSwOn.raise_()
        self.pushBtn_getRealData.raise_()
        self.pushBtn_clrStatus.raise_()

        self.retranslateUi(dlgMain)
        QtCore.QMetaObject.connectSlotsByName(dlgMain)
        dlgMain.setTabOrder(self.lineEdit_IP, self.lineEdit_port)
        dlgMain.setTabOrder(self.lineEdit_port, self.pushBtn_connect)
        dlgMain.setTabOrder(self.pushBtn_connect, self.lineEdit_TCID)
        dlgMain.setTabOrder(self.lineEdit_TCID, self.lineEdit_GPID)
        dlgMain.setTabOrder(self.lineEdit_GPID, self.textEdit_status)

    def retranslateUi(self, dlgMain):
        dlgMain.setWindowTitle(_translate("dlgMain", "CQ1504_PC", None))
        self.label.setText(_translate("dlgMain", "JK_IP", None))
        self.label_2.setText(_translate("dlgMain", "PORT", None))
        self.pushBtn_connect.setText(_translate("dlgMain", "连接", None))
        self.label_3.setText(_translate("dlgMain", "控制器ID", None))
        self.label_4.setText(_translate("dlgMain", "综保ID", None))
        self.lineEdit_GPID.setText(_translate("dlgMain", "1", None))
        self.pushBtn_PreSwOff.setText(_translate("dlgMain", "预分闸", None))
        self.pushBtn_ExecSwOff.setText(_translate("dlgMain", "分闸", None))
        self.pushBtn_PreSwOn.setText(_translate("dlgMain", "预合闸", None))
        self.pushBtn_ExecSwOn.setText(_translate("dlgMain", "合闸", None))
        self.lineEdit_TCID.setText(_translate("dlgMain", "05050605", None))
        self.pushBtn_getRealData.setText(_translate("dlgMain", "实时数据", None))
        self.pushBtn_clrStatus.setText(_translate("dlgMain", "清除", None))

