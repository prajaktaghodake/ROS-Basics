#!/usr/bin/env python

import rospy                            # Import the Python library for ROS
from geometry_msgs.msg import Twist          # Import the Int32 message from the std_msgs

def callback(msg):
    print msg

rospy.init_node('vel_subscriber')
rospy.Subscriber('/cmd_vel' , Twist , callback)
rospy.spin()

