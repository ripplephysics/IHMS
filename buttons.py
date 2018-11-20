import RPi.GPIO as GPIO
import time
import os
import glob
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

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
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
temp = 96

def main():
    up()
    down()
    confirm()
    cancel()

    while True:
          lcd.message('%i' %temp)
         


def up():
    up = GPIO.input(17)
    if up == False:
        temp += 1
        print(temp)
        return temp

def down():
    dwn = GPIO.input(6)
    if dwn == False:
        temp -= 1
        print(temp)
        return temp
def confirm():
    confirm = GPIO.input(21)
    if confirm == False:
       print "confirmed"

def cancel():
    cancel = GPIO.input(19)
    if cancel == False:
       print "canceled"

if __name__ == "__main__":
    main()

#        print( type(temp))

