
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
from  SparkFun_MS5803_I2C import ms5803py # taken from https://pypi.org/project/ms5803py/#

    #/// Version string: be sure to update this version number EVERY time you make any code change,
    #/// period, which isn't just a comment change! Document it in the Software Changelog in the main
    #/// AmboVent readme.
    ##define VERSION_STR "v0.1.0"#
VERSION_STR =  "v0.1.0"
#   // TODO(ElectricRCAircraftGuy): get rid of nearly every single one of these #defines! They should
#   // be `constexpr` variables instead, with the sole exception of ones which are used for variable
#   // compilation, such as those which exclude certain portions of code based on hardware
#   // configuration. (Even this may not be true though, as using bool may still allow the compiler
#   // to optimize out those sections. Do some compilation testing when you get to it).#

#   // System Configuration#

#   /// Set to true for "full system" (the default), or to false for "partial system"--potentiometer
#   /// installed on pulley, no potentiometers... <---? TODO(@ElectricRCAircraftGuy): I request further
#   /// explanation from @nimrod46--please update this description to be more clear.
FULL_CONFIGURATION = False
#/// Set to true if you have installed an I2C pressure sensor
PRESSURE_SENSOR_AVAILABLE = False
# /// Set to true to send unique ID for 10 seconds at startup, false otherwise
CENTRAL_MONITOR_SYSTEM = False
