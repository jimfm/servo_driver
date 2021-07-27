#!/usr/bin/python

from servo_driver import PCA9685
import time

if __name__=='__main__':

  import sys
  snum = 0
  pnum = 0
  try:
    snum = int(sys.argv[1])
    pnum = int(sys.argv[2])
  except IndexError:
    print("There was an error with the passed in args")
    exit()

  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(50)

  pwm.setServoPulse(snum,pnum)   
  print(f"Position 0 {pnum}")
