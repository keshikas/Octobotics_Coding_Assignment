#!/usr/bin/env python
  
import rospy
from std_msgs.msg import String
from inverted_pendulum_sim.msg import ControlForce
from math import sin,pi 
import matplotlib.pyplot as plot
import numpy as np
from scipy import signal
def talker ():
 pub = rospy.Publisher('/inverted_pendulum/control_force', ControlForce, queue_size=10)
 rospy.init_node('control_talker', anonymous=True)
 rate = rospy.Rate(10) # 10hz
 cnt=ControlForce()
 x = np. zeros(100)
 x = np.linspace(0, 200,10000)
 y = x.astype(np.float)
 y =0.5*np.sin(x)
 cart_acc=y/2
 
 #Fs = 2000
 #f = 100
 #sample = Fs/f
 plot.title('cart accelaration')
 plot.plot(x,cart_acc)
 plot.ylabel('cart accelaration')
 plot.show()
 
 
  
 while not rospy.is_shutdown(): 
  for x in range(0,100):
   #y=100*np.sin(2 * pi * f * x / Fs)
   #print(y)
   cnt.force=y[x]
   rospy.loginfo(cnt)
   pub.publish(cnt)
   rate.sleep()
  
if __name__ == '__main__':
 try:
  talker()
 except rospy.ROSInterruptException:
   pass
