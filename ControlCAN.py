# -*- coding: utf-8 -*-

from ctypes import *

class VCI_BOARD_INFO(Structure):
  _fileds_ = [
              ("hw_Version", c_ushort),
              ("fw_Version", c_ushort),
              ("dr_Version", c_ushort),
              ("in_Version", c_ushort),
              ("irq_Num",    c_ushort),
              ("can_Num",    c_byte),
              ("str_Serial_Num", c_char * 20),
              ("str_hw_Type",    c_char * 40),
              ("Reserved",       c_ushort * 4)
  ]

class VCI_CAN_OBJ(Structure):
  _fileds_ = [
              ("ID",          c_uint),
              ("TimeStamp",   c_uint),
              ("TimeFlag",    c_byte),
              ("SendType",    c_byte),
              ("RemoteFlag",  c_byte),
              ("ExternFlag",  c_byte),
              ("DataLen",     c_byte),
              ("Data",        c_byte * 8),
              ("Reserved",    c_byte * 3)
  ]

class VCI_CAN_STATUS(Structure):
  _fileds_ = [
              ("ErrInterrupt", c_char),
              ("regMode",      c_char),
              ("regStatus",    c_char),
              ("regALCapture", c_char),
              ("regECCapture", c_char),
              ("regEWLimit",   c_char),
              ("regRECounter", c_char),
              ("regTECounter", c_char),
              ("Reserved",     c_int)
  ]

class VCI_ERR_INFO(Structure):
  _fileds_ = [
              ("ErrCode",         c_uint),
              ("Passive_ErrData", c_byte * 3),
              ("ArLost_ErrData",  c_byte)
  ]

class VCI_INIT_CONFIG(Structure):
  _fileds_ = [
              ("AccCode",   c_int),
              ("AccMask",   c_int),
              ("Reserved",  c_int),
              ("Filter",    c_char),
              ("Timing0",   c_char),
              ("Timing1",   c_char),
              ("Mode",      c_char)
  ]

class VCI_FILTER_RECORD(Structure):
  _fileds_ = [
              ("ExtFrame",   c_int),
              ("Start",      c_int),
              ("End",        c_int)
  ]

#ÆäËû
class VCI_BOARD_INFO1(Structure):
  _fileds_ = [
             ("hw_Version", c_ushort),
             ("fw_Version", c_ushort),
             ("dr_Version", c_ushort),
             ("in_Version", c_ushort),
             ("irq_Num",    c_ushort),
             ("can_Num",    c_byte),
             ("Reserved",   c_byte),
             ("str_Serial_Num",  c_char * 8),
             ("str_hw_Type",     c_char * 16),
             ("str_Usb_Serial",  c_char * 16)
  ]

class VCI_BOARD_INFO2(Structure):
  _fileds_ = [
             ("hw_Version", c_ushort),
             ("fw_Version", c_ushort),
             ("dr_Version", c_ushort),
             ("in_Version", c_ushort),
             ("irq_Num",    c_ushort),
             ("can_Num",    c_byte),
             ("Reserved",   c_byte),
             ("str_Serial_Num",  c_char * 8),
             ("str_hw_Type",     c_char * 16),
             ("str_Usb_Serial",  c_char * 40)
  ]


