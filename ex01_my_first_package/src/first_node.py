#!/usr/bin/python

import rospy

rospy.init_node('first_node')    
rate = rospy.Rate(2)

while not rospy.is_shutdown():
	print "this is my first node"
	rate.sleep()

