#!/usr/bin/python

from servo_driver import PCA9685
import time

if __name__=='__main__':

  import sys
  snum = 0
  try:
    snum = int(sys.argv[1])
  except IndexError:
    print("There was an error with the passed in args")
    exit()

  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(50)
  
  pmin = 600
  pmax = 2400
  pstep = 20
  while True:
    for i in range(pmin,pmax,pstep):  
      pwm.setServoPulse(snum,i)   
      print(f"Position 1 {i}")
      time.sleep(0.05)     
    
    for i in range(pmax,pmin,-pstep):
      pwm.setServoPulse(snum,i)
      print(f"Position 2 {i}") 
      time.sleep(0.05)  
