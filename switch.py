#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import glob
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO


#lcd and sensor settings
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir =  '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

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


#gpio settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
channel = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

#functions
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
       temp_string = lines[1][equals_pos+2:]
       temp_c = float(temp_string) / 1000.0
       temp_f = temp_c * 9.0 / 5.0 + 32.0
       return temp_f

def temp_alert():
   ta = read_temp()
#this needs to be if elif otherwise it goes nuts
   if ta > 84:
      print "temp alert"
   elif ta < 84:
      print " "
      return temp_alert



#########################3
#power on  screen
lcd.message('Welcome to IHMS')
time.sleep(5.0)
lcd.clear()
lcd.message('use default\n settings?')

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#############################

while True:
    yes = GPIO.input(21)
    no = GPIO.input(19)
    if yes == False:
        lcd.clear()
        lcd.message('default\nselected')
        time.sleep(0.2)
#        os.system('python moisture2.py') 
        os.system('python temp.py')
    elif no == False:
        lcd.clear()
        lcd.message('define\nparameters')
        time.sleep(0.2)
        
