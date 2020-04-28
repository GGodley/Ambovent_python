
#This code is a python implementation of the AMbovent Arduino(C) project.
#
    #THIS CODE WAS WRITTEN FOR TESTING AND RUNNING A HOME-MADE VENTILATION DEVICE.
    #IT IS NOT TESTED FOR SAFETY AND NOT APPROVED FOR USE IN ANY CLINICAL, MEDICAL OR COMERCIAL DEVICE.
    #IT IS NOT APPROVED BY ANY REGULATORY AUTHORITY.
    #USE ONLY AT YOUR OWN RISK.
    #To start calibrations:
    #First enter the maintenance setup menu by pressing the TEST button for 3 seconds.
    #Using the RATE potentiometer select the calibration required and press TEST to select.
    #Follow instructions on the screen.
    #For the Arm range calibration:
    #Use the Rate potentiometer to move the arm up/down.
#*/

from EEPROM import EEPROM  # R/W/CLR Taken from https://www.instructables.com/id/Raspberry-Pi-Python-EEPROM-Programmer/
from LCI2C import liquidcrystal_i2c # taken form https://github.com/pl31/python-liquidcrystal_i2c/tree/master/liquidcrystal_i2c
from  pigpio import servo #taken from https://www.raspberrypi.org/forums/viewtopic.php?t=82142
from  SparkFun_MS5803_I2C
