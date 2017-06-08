# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import ui_main

import binascii
import threading
import array

class MainDlg(QDialog, ui_main.Ui_dlgMain):
  __USBCAN = None
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def __init__(self, parent=None):
    super(MainDlg, self).__init__(parent)
    self.setupUi(self)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

app = QApplication(sys.argv)
mainDlg = MainDlg()
mainDlg.show()
app.exec_()



