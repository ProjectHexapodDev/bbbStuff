#!/usr/bin/env python
"""
"""

from glob import glob
import logging
import os
from utilities import clamp, getPercentageIntoRange, readInt
import logging
import math

log = logging.getLogger(__name__)

"""
 Get an ADC reading representing a string pot value
 Map that value to an angle based on allowable range
 of pot value and angle for that joint
"""
def strPot_to_angle(strPot, potRange, pistonLengthRange, offsets, angleOffset):
  #  import pdb; pdb.set_trace()
  strPot = clamp(potRange, strPot) 
  potSpan = potRange[1] - potRange[0]
  pistonLengthSpan = pistonLengthRange[1] - pistonLengthRange[0]
  pistonLength = (((strPot - potRange[0]) * pistonLengthSpan)/ potSpan ) + pistonLengthRange[0]
  # law of cosines
  jointAngle = math.acos((offsets[0]**2 + offsets[1]**2 - pistonLength**2)/(2 * offsets[0] * offsets[1]))
  
  # Go from angle of triangle to angle from Dead Bug position
  adjustedJointAngle = jointAngle + angleOffset 
  return adjutedJointAngle 

def readAin(pinName, jointRange):
  raw = readInt(pinName)
  raw = clamp(jointRange, raw)
  return getPercentageIntoRange(jointRange, float(raw))

def getAinPinName(pin):
  hits = glob("/sys/bus/iio/devices/iio:device?/in_voltage%s_raw" % pin)
  if hits:
    return hits[0]
  else:
    log.fatal("Could not find ADC pin %s, double check that the firmware loaded..." % pin)
    from pwm_utilities import stopEverythingAndQuit
    stopEverythingAndQuit()

AIN3 = getAinPinName(3)
AIN4 = getAinPinName(4)
AIN5 = getAinPinName(5)
KNEE_RANGE = (0, 1024)  # these values were pulled out of my ass
ELBOW_RANGE = (1420, 3570)  # these values came from a run of calibrate.py
SHOULDER_RANGE = (845, 2736)  # these values were measured manually
# 2465
if __name__ == "__main__":
  pass
