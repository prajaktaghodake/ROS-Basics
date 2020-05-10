#!/usr/bin/env python

import rospy                            # Import the Python library for ROS
from geometry_msgs.msg import Twist          # Import the Int32 message from the std_msgs

rospy.init_node('vel_publisher')      # Initiate a Node named 'topic_publisher'
pub = rospy.Publisher('/cmd_vel', Twist) # Create a Publisher object, that will publish
                                        # messages of type Int32

rate = rospy.Rate(2)                    # Set a publish rate of 2 Hz
twist = Twist()
twist.linear.x = 0.1
twist.angular.z = 0                     # Create a var of type Int32


while not rospy.is_shutdown():          # Create a loop that will go until someone stops the programm
    pub.publish(twist)                  # Publish the message within the 'count' variable
                                        # Increment 'count' variable
    rate.sleep()                        # Make sure the publish rate maintains at 2 Hz
