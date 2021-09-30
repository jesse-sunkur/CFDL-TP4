#!/usr/bin/env python
# Author: Jesse Sunkur

import sys
import time
from std_msgs.msg import Bool
from std_msgs.msg import Int32
import std_srvs
from std_srvs.srv import Empty
import rospy
import rosservice

def service(msg):
    global_loc = rospy.ServiceProxy('/global_localization', True)
     
#rosservice.call_service('/global_localization',True)
#rosservice.call_service('/request_nomotion_update',True)

if __name__ == '__main__':
    rospy.init_node('service_node')
    rospy.Subscriber("/X",Empty,service)

rospy.spin()
