#!/usr/bin/env python

import rospy
from goal_publisher.msg import PointArray

def callback(msg):
    print("Point 0: x: {a}, y: {b}, z: {c}".format(a= msg.goals[0].x,b=msg.goals[0].y,c=msg.goals[0].z))
    print("Point 1: x: {d}, y: {e}, z: {f}".format(d= msg.goals[1].x,e=msg.goals[1].y,f=msg.goals[1].z))
    print("Point 2: x: {g}, y: {h}, z: {i}".format(g= msg.goals[2].x,h=msg.goals[2].y,i=msg.goals[2].z))
    
    
rospy.init_node('goal_launch')
rospy.Subscriber('/points', PointArray, callback)
rospy.spin()
