#!/usr/bin/env python
    
from __future__ import print_function
   
import sys
import rospy
from inverted_pendulum_sim.srv import *
    
def set_param_client(p_mass,p_length,c_mass,theta_0,theta_dot_0,theta_dot_dot_0,cart_x_0,cart_x_dot_0,cart_x_dot_dot_0):
       rospy.wait_for_service('inverted_pendulum/set_params')
       try:
        inverted_pendulum_set_params = rospy.ServiceProxy('inverted_pendulum/set_params', SetParams)
        resp1 = inverted_pendulum_set_params(p_mass,p_length,c_mass,theta_0,theta_dot_0,theta_dot_dot_0,cart_x_0,cart_x_dot_0,cart_x_dot_dot_0)
        
        return resp1
       except rospy.ServiceException as e:
         print("Service call failed: %s"%e)
  
def usage():
   return "%s [x y]"%sys.argv[0]
  
if __name__ == "__main__":
 if len(sys.argv) >1:
  p_mass = int(sys.argv[1])
  p_length= int(sys.argv[2])
  c_mass=int(sys.argv[3])
  theta_0=int(sys.argv[4])
  theta_dot_0=int(sys.argv[5])
  theta_dot_dot_0 =int(sys.argv[6])
  cart_x_0=int(sys.argv[7])
  cart_x_dot_0=int(sys.argv[8])
  cart_x_dot_dot_0=int(sys.argv[9])
  print("entered main")
                     
             
 else:
          print("didnt entered main")
          print(usage())
          sys.exit(1)
      
 p_mass=2.0
 p_length=300.0
 c_mass=0.5
 theta_0=300.0
 theta_dot_0=0.0
 theta_dot_dot_0=0.0
 cart_x_0=0.0
 cart_x_dot_0=0.0
 cart_x_dot_dot_0=0.0     
 v=set_param_client(p_mass,p_length,c_mass,theta_0,theta_dot_0,theta_dot_dot_0,cart_x_0,cart_x_dot_0,cart_x_dot_dot_0)
 print("%s,%s"%(v.success,v.message))
  
  

