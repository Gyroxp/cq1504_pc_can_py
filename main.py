# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import ui_main

#import binascii
#import array
import threading
import struct
import ctypes
import ControlCAN

class MainDlg(QDialog, ui_main.Ui_dlgMain):
  __USBCAN = None
  __DevTypeList = {"DEV_USBCAN"  : 3,
                   "DEV_USBCAN2" : 4 }
  __devType = None
  __devIdx  = None
  __Chn     = None
  __timer   = None
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def __init__(self, parent=None):
    super(MainDlg, self).__init__(parent)
    self.setupUi(self)

    self.cmb_devType.addItem("DEV_USBCAN")
    self.cmb_devType.addItem("DEV_USBCAN2")
    self.cmb_devType.setCurrentIndex(1)

    self.cmb_Chn.addItem("1")
    self.cmb_Chn.addItem("2")
    self.cmb_Chn.setCurrentIndex(0)

    self.lineEdit_AccCode.setText("00000000")
    self.lineEdit_AccMask.setText("FFFFFFFF")
    self.lineEdit_Time0.setText("00")
    self.lineEdit_Time1.setText("1C")

    self.cmb_Filter.addItem(u"接收全部类型")
    self.cmb_Filter.addItem(u"只接收标准帧")
    self.cmb_Filter.addItem(u"只接收扩展帧")
    self.cmb_Filter.setCurrentIndex(0)

    self.cmb_Mode.addItem(u"正常")
    self.cmb_Mode.addItem(u"只听")
    self.cmb_Mode.addItem(u"自测")
    self.cmb_Mode.setCurrentIndex(0)

    self.pushBtn_startCAN.setDisabled(1)

    try:
      self.__USBCAN = ctypes.windll.LoadLibrary(".\ControlCAN.dll")
      self.pushBtn_connect.setDisabled(0)
    except:
      QMessageBox.information(self, u"错误",  u"找不到ControlCAN.dll")
      sys.exit

    boardInfo = ControlCAN.VCI_BOARD_INFO1()
    x = self.__USBCAN.VCI_FindUsbDevice(ctypes.byref(boardInfo))
    for i in range(x):
      self.cmb_devIndex.addItem(str(i))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #自动关联的槽函数
  @pyqtSlot()
  def on_pushBtn_connect_clicked(self):
    if self.pushBtn_connect.text() == u'连接':
      text = self.cmb_devType.currentText()
      text = text.toLatin1()
      str = ""
      for i in text:
        str += i
      self.__devType = self.__DevTypeList.get(str)
      
      self.__devIdx = self.cmb_devIndex.currentIndex()
      err = self.__USBCAN.VCI_OpenDevice(self.__devType, self.__devIdx, 0)
      if err == 1:
         #QMessageBox.information(self, u"恭喜",  u"连接成功!")
         self.cmb_devType.setDisabled(1)
         self.cmb_devIndex.setDisabled(1)
         self.cmb_Chn.setDisabled(1)
         self.pushBtn_startCAN.setDisabled(0)
         self.pushBtn_connect.setText(u'关闭')
      else:
        QMessageBox.information(self, u"错误",  u"找不到设备")

    elif self.pushBtn_connect.text() == u'关闭':
      self.__USBCAN.VCI_CloseDevice(self.__devType, self.__devIdx)
      self.cmb_devType.setDisabled(0)
      self.cmb_devIndex.setDisabled(0)
      self.cmb_Chn.setDisabled(0)
      self.pushBtn_startCAN.setDisabled(1)
      self.pushBtn_connect.setText(u'连接')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  @pyqtSlot()
  def on_pushBtn_startCAN_clicked(self):
    self.__Chn = self.cmb_Chn.currentIndex()

    initcfg = ControlCAN.VCI_INIT_CONFIG()  #AccCode=0, AccMask=0xFFFFFFFF, Reserved=0, Filter=1, Timing0=0, Timing1=0x1c, Mode=2)
    initcfg.AccCode = 0
    initcfg.AccMask = 0xFFFFFFFF
    initcfg.Reserved = 0
    initcfg.Filter  = 0
    initcfg.Timing0 = 0
    initcfg.Timing1 = 0x1C
    initcfg.Mode    = 2
    err = self.__USBCAN.VCI_InitCAN(self.__devType, self.__devIdx, self.__Chn, ctypes.addressof(initcfg))
    if err == 1:
      self.__USBCAN.VCI_StartCAN(self.__devType, self.__devIdx, self.__Chn)
      self.__timer = threading.Timer(0.1, self.can_rx)
      self.__timer.start()
    elif err == 0:
      QMessageBox.information(self, u"错误",  u"初始化失败")
    elif err == -1:
      QMessageBox.information(self, u"错误",  u"设备不存在")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  @pyqtSlot()
  def on_pushBtn_txdata_clicked(self):
    canobj = ControlCAN.VCI_CAN_OBJ()  #ID=8, TimeStamp=0, TimeFlag=0, SendType=0, RemoteFlag=0, ExternFlag=0, DataLen=8, Data='1234567')
    canobj.ID = 88
    #canobj.TimeStamp
    #canobj.TimeFlag
    #canobj.SendType
    canobj.RemoteFlag = 0    #1 远程 0 数据
    canobj.ExternFlag = 0    #1 扩展 0 标准
    canobj.DataLen = 4
    canobj.Data = "2345"
    frameNum = self.__USBCAN.VCI_Transmit(self.__devType, self.__devIdx, self.__Chn, ctypes.addressof(canobj), 1)
    if frameNum == -1:
      QMessageBox.information(self, u"错误",  u"设备错误")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def can_rx(self):
    rxobj = ControlCAN.VCI_CAN_OBJ()
    res = self.__USBCAN.VCI_Receive(self.__devType, self.__devIdx, self.__Chn, ctypes.addressof(rxobj), 1000, 100);
    if res > 0:
      print res

    self.__timer = threading.Timer(0.1, self.can_rx)
    self.__timer.start()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

app = QApplication(sys.argv)
mainDlg = MainDlg()
mainDlg.show()
app.exec_()



