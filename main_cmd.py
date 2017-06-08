# -*- coding: utf-8 -*-
#-----------------------------File Information--------------------------------
#File name:    cmd.py
#Created by:   Liu Jing-wei
#Created date: 2017-01-03
#Version Info:
#Descriptions:
#-----------------------------------------------------------------------------
#Modified by:
#Modified date:
#Descriptions:
#-----------------------------------------------------------------------------

import switch as switch
import mycan

#-------------------------------------------------------
print('welcome\n')

while True:
  if exit == 1:
    break

  cmd = raw_input("cmd:")
  for case in switch.switch(cmd):
    if case('e'):
      print 'exit'
      exit = 1
      break
    if case('s'):
      mycan.startCAN()
      break
    if case():
      print "command else!\n"

print('End!\n')
