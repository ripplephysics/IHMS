import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD
import os
import glob

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

#initlize the pins above
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
lcd_columns, lcd_rows, lcd_backlight)

lcd.clear()

#gpio setup
channel = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)



def callback(channel):
    if GPIO.input(channel):
	lcd.clear()
        print "Moisture Alert!"
        lcd.message('Moisture Alert!')
    else:
        print "Moisture Alert!"

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)


while True:
        time.sleep(1)




