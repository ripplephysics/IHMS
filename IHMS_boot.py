#!/usr/bin/python
import os
import glob
import time
import sys
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

#LCD intilize
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

#sensor initlize
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

#moisture sensor

channel = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

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
       lcd.clear()
       lcd.message("temp alert!")
       lcd.set_cursor(1,2)
       lcd.message("Curent temp > % " %ta)
    elif ta < 84:
       print " "
    return temp_alert






print ("Welcome to the Infant Health Monitoring System")


def ask_user():
    check = str(raw_input("Do you wish to use Default settings? (Y/N): ")).lower().strip()
    try:
        if check[0] == 'y':
            print("Default settings selected")
            os.system('python temp2.py')
            return null
        elif check[0] == 'n':
             print("User specified settings selected")
            # temp_in = float(raw_input("Define temp input: "))
           #  moisture_in=str(raw_input("Moisture Sensor On? (Y/N )")).lower().strip()
            # motion_in=str(raw_input("Motion Sensor On? (Y/N )")).lower().strip()
           #  print (temp_in, moisture_in, motion_in)
           #  print( type(temp_in))
           #  print(type(moisture_in))
           #  print(type(motion_in))
             #return null
            #pass these into the next program similar to###temp.py###



             os.system('python user_boot.py')
             return null;
        else:
            print('Invalid Input')
            return ask_user()
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return ask_user()


#bad syntax
#while False:
   # lcd.clear()
   # temp_text = (read_temp())
   # lcd.message('%s' % (temp_text))
   # lcd.set_cursor(2,1)
   # if temp_text > 84:
  #     lcd.message('Temp Alert!')
 #   elif temp_text < 84:
#         lcd.message('')  

while True:
    print(ask_user())
    if ask_user() is done:
       break
    
