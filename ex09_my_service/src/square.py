#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import radians

class DrawASquare():
    def __init__(self):


        rospy.on_shutdown(self.shutdown)

        self.cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=10)


        rate = rospy.Rate(5);
        move_cmd = Twist()
        move_cmd.linear.x = 0.2
        turn_cmd = Twist()
        turn_cmd.linear.x = 0
        turn_cmd.angular.z = radians(36);


	itr = 0
        while not rospy.is_shutdown():
	    rospy.loginfo("Moving Forward")
            for x in range(0,10):
                self.cmd_vel.publish(move_cmd)
                rate.sleep()
	    rospy.loginfo("Going Around")
            for x in range(0,14):
                self.cmd_vel.publish(turn_cmd)
                rate.sleep()
	    itr = itr + 1
	    if(itr == 4):
                itr = 0
	    if(itr == 0):
                rospy.loginfo("TurtleBot should be close to the original starting position (but it's probably way off)")

    def shutdown(self):
        rospy.loginfo("Stop")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        rospy.init_node('squaremove', anonymous=False)
        DrawASquare()
    except:
        rospy.loginfo("node terminated.")
