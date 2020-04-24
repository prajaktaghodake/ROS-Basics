#! /usr/bin/env python

import rospy
from goal_publisher.msg import PointArray

def callback(msg):
    print msg

rospy.init_node('goal_launch')
rospy.Subscriber('/points',PointArray, callback)
rospy.spin()
