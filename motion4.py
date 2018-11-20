import time

# Import the ADXL345 module.
import Adafruit_ADXL345


# Create an ADXL345 instance.
accel = Adafruit_ADXL345.ADXL345()
print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    x, y, z = accel.read()
    print('X={0}, Y={1}, Z={2}'.format(x, y, z))
    # Wait half a second and repeat.
    if x > 180:
       print "motion detected in x axis" 
    elif y > 180:
         print "motion detected in y axis"
    elif z > 180:
         print "motion detected in z axis"
    time.sleep(5)
