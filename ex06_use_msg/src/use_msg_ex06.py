#!/usr/bin/env python

import rospy                            # Import the Python library for ROS
from ex06_age_msg.msg import Age          # Import the Int32 message from the std_msgs

rospy.init_node('use_msg')      # Initiate a Node named 'topic_publisher'
pub = rospy.Publisher('age_topic', Age) # Create a Publisher object, that will publish
                                        # messages of type Int32

rate = rospy.Rate(2)                    # Set a publish rate of 2 Hz
age = Age()
age.years = 25 
age.months = 06
age.days = 16                     # Create a var of type Int32
                          

while not rospy.is_shutdown():          # Create a loop that will go until someone stops the programm                  
    pub.publish(age)                  # Publish the message within the 'count' variable
                                        # Increment 'count' variable
    rate.sleep()                        # Make sure the publish rate maintains at 2 Hz

