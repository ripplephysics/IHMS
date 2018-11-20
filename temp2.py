import os
import glob
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import Adafruit_ADXL345


# Create an ADXL345 instance.
accel = Adafruit_ADXL345.ADXL345()


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

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

channel = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)




lcd.message("Welcome to\nIHMS")
time.sleep(5)
lcd.clear()
lcd.message("Preset\nSettings")
time.sleep(5)
lcd.clear()




def main():


   # callback(channel)
    while True:
          lcd.clear()
          temp_text = (read_temp())
          lcd.message('%s' % (temp_text))
          time.sleep(1)
          lcd.set_cursor(2,1)
          lcd.clear()
          callback(channel)
          motion()
          lcd.clear()

          if temp_text > 80:
             lcd.message('Temp Alert!')
          elif temp_text < 98:
               lcd.message('')
          time.sleep(1)


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



def callback(channel):
    if GPIO.input(channel):
        lcd.clear()
       # print "Moisture Alert!"
        lcd.message(' Moisture Alert!')
    else:
        print " moisture alert "
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)


def motion():
    accel = Adafruit_ADXL345.ADXL345()
    x, y, z = accel.read()
    if x > 180 or y > 180 or z > 180:
       print "motion detected"
       lcd.clear()
       lcd.message("Motion Detected")
       time.sleep(1)

def malert():
    os.system('email_alert.py')

if __name__ == "__main__":
    main()
