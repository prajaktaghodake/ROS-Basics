#!/usr/bin/env python

import rospy                            # Import the Python library for ROS
from ex06_use_msg.msg import Age          # Import the Int32 message from the std_msgs

rospy.init_node('use_msg')              # Initiate a Node named 'topic_publisher'
age = rospy.Publisher('/my_bio', Age) # Create a Publisher object, that will publish
                                        # messages of type Int32

rate = rospy.Rate(2)                    # Set a publish rate of 2 Hz
pra = Age()
pra.years = 1995
pra.months = 06
pra.days = 16                                        # Create a var of type Int32


while not rospy.is_shutdown():          # Create a loop that will go until someone stops the programm
    age.publish(pra)                  # Publish the message within the 'count' variable
                                        # Increment 'count' variable
    rate.sleep()                        # Make sure the publish rate maintains at 2 Hz
