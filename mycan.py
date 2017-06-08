# -*- coding: utf-8 -*-

import ctypes
import ControlCAN

def startCAN():
  USBCAN = ctypes.windll.LoadLibrary(".\ControlCAN.dll")
  err = USBCAN.VCI_OpenDevice(4, 0, 0)
  if err == 1:
    USBCAN.VCI_CloseDevice(4, 0)
  pass


