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
        dlgMain.resize(800, 540)
        self.frame = QtGui.QFrame(dlgMain)
        self.frame.setGeometry(QtCore.QRect(0, 0, 531, 41))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(178, 14, 36, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(11, 14, 24, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.cmb_devType = QtGui.QComboBox(self.frame)
        self.cmb_devType.setGeometry(QtCore.QRect(41, 12, 100, 20))
        self.cmb_devType.setObjectName(_fromUtf8("cmb_devType"))
        self.cmb_devIndex = QtGui.QComboBox(self.frame)
        self.cmb_devIndex.setGeometry(QtCore.QRect(220, 12, 69, 20))
        self.cmb_devIndex.setObjectName(_fromUtf8("cmb_devIndex"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(320, 14, 36, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cmb_Chn = QtGui.QComboBox(self.frame)
        self.cmb_Chn.setGeometry(QtCore.QRect(362, 12, 69, 20))
        self.cmb_Chn.setObjectName(_fromUtf8("cmb_Chn"))
        self.pushBtn_connect = QtGui.QPushButton(self.frame)
        self.pushBtn_connect.setGeometry(QtCore.QRect(450, 12, 75, 23))
        self.pushBtn_connect.setObjectName(_fromUtf8("pushBtn_connect"))
        self.label_3 = QtGui.QLabel(dlgMain)
        self.label_3.setGeometry(QtCore.QRect(556, 22, 48, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(dlgMain)
        self.label_4.setGeometry(QtCore.QRect(698, 22, 36, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_GPID_1 = QtGui.QLineEdit(dlgMain)
        self.lineEdit_GPID_1.setGeometry(QtCore.QRect(740, 20, 31, 20))
        self.lineEdit_GPID_1.setObjectName(_fromUtf8("lineEdit_GPID_1"))
        self.textEdit_recv = QtGui.QTextEdit(dlgMain)
        self.textEdit_recv.setGeometry(QtCore.QRect(0, 260, 531, 281))
        self.textEdit_recv.setObjectName(_fromUtf8("textEdit_recv"))
        self.lineEdit_TCID_1 = QtGui.QLineEdit(dlgMain)
        self.lineEdit_TCID_1.setGeometry(QtCore.QRect(610, 20, 61, 20))
        self.lineEdit_TCID_1.setObjectName(_fromUtf8("lineEdit_TCID_1"))
        self.pushBtn_clr = QtGui.QPushButton(dlgMain)
        self.pushBtn_clr.setGeometry(QtCore.QRect(450, 230, 75, 23))
        self.pushBtn_clr.setObjectName(_fromUtf8("pushBtn_clr"))
        self.lineEdit_AccCode = QtGui.QLineEdit(dlgMain)
        self.lineEdit_AccCode.setGeometry(QtCore.QRect(69, 70, 80, 20))
        self.lineEdit_AccCode.setText(_fromUtf8(""))
        self.lineEdit_AccCode.setObjectName(_fromUtf8("lineEdit_AccCode"))
        self.label_6 = QtGui.QLabel(dlgMain)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 54, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_AccMask = QtGui.QLineEdit(dlgMain)
        self.lineEdit_AccMask.setGeometry(QtCore.QRect(69, 100, 80, 20))
        self.lineEdit_AccMask.setText(_fromUtf8(""))
        self.lineEdit_AccMask.setObjectName(_fromUtf8("lineEdit_AccMask"))
        self.label_7 = QtGui.QLabel(dlgMain)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 54, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_Time0 = QtGui.QLineEdit(dlgMain)
        self.lineEdit_Time0.setGeometry(QtCore.QRect(230, 70, 31, 20))
        self.lineEdit_Time0.setObjectName(_fromUtf8("lineEdit_Time0"))
        self.label_8 = QtGui.QLabel(dlgMain)
        self.label_8.setGeometry(QtCore.QRect(160, 70, 60, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(dlgMain)
        self.label_9.setGeometry(QtCore.QRect(160, 100, 60, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_Time1 = QtGui.QLineEdit(dlgMain)
        self.lineEdit_Time1.setGeometry(QtCore.QRect(230, 100, 31, 20))
        self.lineEdit_Time1.setObjectName(_fromUtf8("lineEdit_Time1"))
        self.label_10 = QtGui.QLabel(dlgMain)
        self.label_10.setGeometry(QtCore.QRect(272, 70, 48, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(dlgMain)
        self.label_11.setGeometry(QtCore.QRect(290, 100, 24, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.cmb_Filter = QtGui.QComboBox(dlgMain)
        self.cmb_Filter.setGeometry(QtCore.QRect(329, 71, 101, 20))
        self.cmb_Filter.setObjectName(_fromUtf8("cmb_Filter"))
        self.cmb_Mode = QtGui.QComboBox(dlgMain)
        self.cmb_Mode.setGeometry(QtCore.QRect(329, 97, 101, 20))
        self.cmb_Mode.setObjectName(_fromUtf8("cmb_Mode"))
        self.pushBtn_startCAN = QtGui.QPushButton(dlgMain)
        self.pushBtn_startCAN.setGeometry(QtCore.QRect(450, 80, 75, 23))
        self.pushBtn_startCAN.setObjectName(_fromUtf8("pushBtn_startCAN"))
        self.frame_3 = QtGui.QFrame(dlgMain)
        self.frame_3.setGeometry(QtCore.QRect(0, 50, 531, 80))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.frame_4 = QtGui.QFrame(dlgMain)
        self.frame_4.setGeometry(QtCore.QRect(0, 140, 531, 80))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_4.setLineWidth(1)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label_12 = QtGui.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(10, 12, 48, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.cmb_FrameType = QtGui.QComboBox(self.frame_4)
        self.cmb_FrameType.setGeometry(QtCore.QRect(60, 10, 69, 20))
        self.cmb_FrameType.setObjectName(_fromUtf8("cmb_FrameType"))
        self.cmb_FrameFormat = QtGui.QComboBox(self.frame_4)
        self.cmb_FrameFormat.setGeometry(QtCore.QRect(210, 10, 69, 20))
        self.cmb_FrameFormat.setObjectName(_fromUtf8("cmb_FrameFormat"))
        self.lineEdit_ID = QtGui.QLineEdit(self.frame_4)
        self.lineEdit_ID.setGeometry(QtCore.QRect(360, 10, 80, 20))
        self.lineEdit_ID.setObjectName(_fromUtf8("lineEdit_ID"))
        self.label_13 = QtGui.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(160, 12, 48, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(310, 12, 48, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.pushBtn_txdata = QtGui.QPushButton(self.frame_4)
        self.pushBtn_txdata.setGeometry(QtCore.QRect(450, 50, 75, 23))
        self.pushBtn_txdata.setObjectName(_fromUtf8("pushBtn_txdata"))
        self.lineEdit_Data = QtGui.QLineEdit(self.frame_4)
        self.lineEdit_Data.setGeometry(QtCore.QRect(60, 50, 381, 20))
        self.lineEdit_Data.setObjectName(_fromUtf8("lineEdit_Data"))
        self.label_15 = QtGui.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(10, 50, 48, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(dlgMain)
        self.label_16.setGeometry(QtCore.QRect(10, 240, 91, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.pushBtn_baudHelp = QtGui.QPushButton(dlgMain)
        self.pushBtn_baudHelp.setGeometry(QtCore.QRect(220, 230, 75, 23))
        self.pushBtn_baudHelp.setObjectName(_fromUtf8("pushBtn_baudHelp"))
        self.pushBtn_startJump = QtGui.QPushButton(dlgMain)
        self.pushBtn_startJump.setGeometry(QtCore.QRect(620, 170, 75, 23))
        self.pushBtn_startJump.setObjectName(_fromUtf8("pushBtn_startJump"))
        self.label_17 = QtGui.QLabel(dlgMain)
        self.label_17.setGeometry(QtCore.QRect(556, 52, 48, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(dlgMain)
        self.label_18.setGeometry(QtCore.QRect(698, 52, 36, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.lineEdit_TCID_2 = QtGui.QLineEdit(dlgMain)
        self.lineEdit_TCID_2.setGeometry(QtCore.QRect(610, 50, 61, 20))
        self.lineEdit_TCID_2.setObjectName(_fromUtf8("lineEdit_TCID_2"))
        self.lineEdit_GPID_2 = QtGui.QLineEdit(dlgMain)
        self.lineEdit_GPID_2.setGeometry(QtCore.QRect(740, 50, 31, 20))
        self.lineEdit_GPID_2.setText(_fromUtf8(""))
        self.lineEdit_GPID_2.setObjectName(_fromUtf8("lineEdit_GPID_2"))
        self.label_19 = QtGui.QLabel(dlgMain)
        self.label_19.setGeometry(QtCore.QRect(698, 82, 36, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.lineEdit_TCID_3 = QtGui.QLineEdit(dlgMain)
        self.lineEdit_TCID_3.setGeometry(QtCore.QRect(610, 80, 61, 20))
        self.lineEdit_TCID_3.setObjectName(_fromUtf8("lineEdit_TCID_3"))
        self.label_20 = QtGui.QLabel(dlgMain)
        self.label_20.setGeometry(QtCore.QRect(556, 82, 48, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.lineEdit_GPID_3 = QtGui.QLineEdit(dlgMain)
        self.lineEdit_GPID_3.setGeometry(QtCore.QRect(740, 80, 31, 20))
        self.lineEdit_GPID_3.setText(_fromUtf8(""))
        self.lineEdit_GPID_3.setObjectName(_fromUtf8("lineEdit_GPID_3"))
        self.lineEdit_GPID_4 = QtGui.QLineEdit(dlgMain)
        self.lineEdit_GPID_4.setGeometry(QtCore.QRect(742, 108, 31, 20))
        self.lineEdit_GPID_4.setText(_fromUtf8(""))
        self.lineEdit_GPID_4.setObjectName(_fromUtf8("lineEdit_GPID_4"))
        self.lineEdit_TCID_4 = QtGui.QLineEdit(dlgMain)
        self.lineEdit_TCID_4.setGeometry(QtCore.QRect(612, 108, 61, 20))
        self.lineEdit_TCID_4.setObjectName(_fromUtf8("lineEdit_TCID_4"))
        self.label_21 = QtGui.QLabel(dlgMain)
        self.label_21.setGeometry(QtCore.QRect(558, 110, 48, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(dlgMain)
        self.label_22.setGeometry(QtCore.QRect(700, 110, 36, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.lineEdit_GPID_5 = QtGui.QLineEdit(dlgMain)
        self.lineEdit_GPID_5.setGeometry(QtCore.QRect(742, 138, 31, 20))
        self.lineEdit_GPID_5.setText(_fromUtf8(""))
        self.lineEdit_GPID_5.setObjectName(_fromUtf8("lineEdit_GPID_5"))
        self.lineEdit_TCID_5 = QtGui.QLineEdit(dlgMain)
        self.lineEdit_TCID_5.setGeometry(QtCore.QRect(612, 138, 61, 20))
        self.lineEdit_TCID_5.setObjectName(_fromUtf8("lineEdit_TCID_5"))
        self.label_23 = QtGui.QLabel(dlgMain)
        self.label_23.setGeometry(QtCore.QRect(558, 140, 48, 16))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(dlgMain)
        self.label_24.setGeometry(QtCore.QRect(700, 140, 36, 16))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.frame_3.raise_()
        self.frame.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit_GPID_1.raise_()
        self.lineEdit_TCID_1.raise_()
        self.textEdit_recv.raise_()
        self.pushBtn_clr.raise_()
        self.lineEdit_AccCode.raise_()
        self.label_6.raise_()
        self.lineEdit_AccMask.raise_()
        self.label_7.raise_()
        self.lineEdit_Time0.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.lineEdit_Time1.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.cmb_Filter.raise_()
        self.cmb_Mode.raise_()
        self.pushBtn_startCAN.raise_()
        self.frame_4.raise_()
        self.label_16.raise_()
        self.pushBtn_baudHelp.raise_()
        self.pushBtn_startJump.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.lineEdit_TCID_2.raise_()
        self.lineEdit_GPID_2.raise_()
        self.label_19.raise_()
        self.lineEdit_TCID_3.raise_()
        self.label_20.raise_()
        self.lineEdit_GPID_3.raise_()
        self.lineEdit_GPID_4.raise_()
        self.lineEdit_TCID_4.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.lineEdit_GPID_5.raise_()
        self.lineEdit_TCID_5.raise_()
        self.label_23.raise_()
        self.label_24.raise_()

        self.retranslateUi(dlgMain)
        QtCore.QMetaObject.connectSlotsByName(dlgMain)
        dlgMain.setTabOrder(self.pushBtn_connect, self.lineEdit_TCID_1)
        dlgMain.setTabOrder(self.lineEdit_TCID_1, self.lineEdit_GPID_1)
        dlgMain.setTabOrder(self.lineEdit_GPID_1, self.textEdit_recv)

    def retranslateUi(self, dlgMain):
        dlgMain.setWindowTitle(_translate("dlgMain", "CQ1504_PC_CAN", None))
        self.label_2.setText(_translate("dlgMain", "索引号", None))
        self.label.setText(_translate("dlgMain", "类型", None))
        self.label_5.setText(_translate("dlgMain", "第几路", None))
        self.pushBtn_connect.setText(_translate("dlgMain", "连接", None))
        self.label_3.setText(_translate("dlgMain", "控制器ID", None))
        self.label_4.setText(_translate("dlgMain", "综保ID", None))
        self.lineEdit_GPID_1.setText(_translate("dlgMain", "1", None))
        self.lineEdit_TCID_1.setText(_translate("dlgMain", "05050605", None))
        self.pushBtn_clr.setText(_translate("dlgMain", "清除", None))
        self.label_6.setText(_translate("dlgMain", "验收码:0x", None))
        self.label_7.setText(_translate("dlgMain", "屏蔽码:0x", None))
        self.lineEdit_Time0.setText(_translate("dlgMain", "00", None))
        self.label_8.setText(_translate("dlgMain", "定时器0:0x", None))
        self.label_9.setText(_translate("dlgMain", "定时器1:0x", None))
        self.lineEdit_Time1.setText(_translate("dlgMain", "00", None))
        self.label_10.setText(_translate("dlgMain", "滤波方式", None))
        self.label_11.setText(_translate("dlgMain", "模式", None))
        self.pushBtn_startCAN.setText(_translate("dlgMain", "启动CAN", None))
        self.label_12.setText(_translate("dlgMain", "帧类型", None))
        self.lineEdit_ID.setText(_translate("dlgMain", "123", None))
        self.label_13.setText(_translate("dlgMain", "帧格式", None))
        self.label_14.setText(_translate("dlgMain", "帧ID: 0x", None))
        self.pushBtn_txdata.setText(_translate("dlgMain", "发送", None))
        self.lineEdit_Data.setText(_translate("dlgMain", "00 01 02 03 04 05 06 07", None))
        self.label_15.setText(_translate("dlgMain", "数据", None))
        self.label_16.setText(_translate("dlgMain", "接收到的数据", None))
        self.pushBtn_baudHelp.setText(_translate("dlgMain", "波特率帮助", None))
        self.pushBtn_startJump.setText(_translate("dlgMain", "模拟故障", None))
        self.label_17.setText(_translate("dlgMain", "控制器ID", None))
        self.label_18.setText(_translate("dlgMain", "综保ID", None))
        self.lineEdit_TCID_2.setText(_translate("dlgMain", "05050605", None))
        self.label_19.setText(_translate("dlgMain", "综保ID", None))
        self.lineEdit_TCID_3.setText(_translate("dlgMain", "05050605", None))
        self.label_20.setText(_translate("dlgMain", "控制器ID", None))
        self.lineEdit_TCID_4.setText(_translate("dlgMain", "05050605", None))
        self.label_21.setText(_translate("dlgMain", "控制器ID", None))
        self.label_22.setText(_translate("dlgMain", "综保ID", None))
        self.lineEdit_TCID_5.setText(_translate("dlgMain", "05050605", None))
        self.label_23.setText(_translate("dlgMain", "控制器ID", None))
        self.label_24.setText(_translate("dlgMain", "综保ID", None))

