#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
import os
import glob
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
from subprocess import *
from time import sleep, strftime
from datetime import datetime
lcd_rs = 26
lcd_en = 24
lcd_d4 = 22
lcd_d5 = 18
lcd_d6 = 16
lcd_d7 = 12
lcd_backlight = 4
lcd_columns = 16
lcd_rows = 2 
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
lcd_columns, lcd_rows, lcd_backlight)



cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"



def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

while 1:
        lcd.clear()
        ipaddr = run_cmd(cmd)
        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
        lcd.message('IP %s' % ( ipaddr ) )
        sleep(2)

