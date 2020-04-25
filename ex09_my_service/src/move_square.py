#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time


class MoveBB8():

    def __init__(self):
        self.vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.ctrl_c = False
        self.rate = rospy.Rate(10)  # 10Hz
        rospy.on_shutdown(self.shutdownhook)

    def publish_once_in_cmd_vel(self,cmd):
        """
        This is because publishing in topics sometimes fails the first time you publish.
        In continuous publishing systems, this is no big deal, but in systems that publish only
        once, it IS very important.
        """
        while not self.ctrl_c:
            connections = self.vel_publisher.get_num_connections()
            if connections > 0:
                self.vel_publisher.publish(cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()

    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.stop_robot()
        self.ctrl_c = True

    def stop_robot(self):
        rospy.loginfo("shutdown time! Stop the robot")
        cmd = Twist()
        cmd.linear.x = 0.0
        cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel(cmd)

    def move_x_time(self,moving_time,linear_speed=0.2,angular_speed =0.0):
        cmd = Twist()
        # Initilize velocities
        cmd.linear.x = linear_speed
        cmd.angular.z = angular_speed
        rospy.loginfo("Moving forwards")

        # Publish the velocity
        self.publish_once_in_cmd_vel(cmd)
        time.sleep(moving_time)
        self.stop_robot()
        rospy.loginfo("######## Finished Moving forwards")

    def move_square(self):
        i=0
        while not self.ctrl_c and i < 4:
            # Move forwards
            self.move_x_time(moving_time=4.0,linear_speed=0.2,angular_speed=0.0)
            # stop
            self.move_x_time(moving_time=4.0,linear_speed=0.0,angular_speed=0.0)
            # turn
            self.move_x_time(moving_time=12.72,linear_speed=0.0,angular_speed=0.2)     
            # stop
            self.move_x_time(moving_time=0.15,linear_speed=0.0,angular_speed=0.0)
            i += 1
        rospy.loginfo("######## Finished Moving in square")

if __name__ == '__main__':
    
    rospy.init_node('move_robot_test', anonymous=True)
    robot_object = MoveBB8()
    try:
        robot_object.move_square()

    except rospy.ROSInterruptException:
        pass

