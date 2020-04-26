#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import radians
from ex10_my_srv_msg.srv import MyServiceMsg, MyServiceMsgResponse

def my_callback(request):
    my_response = MyServiceMsgResponse()
    for i in range(request.repetitions):
        count = 0
        while not count == 4:
            rospy.loginfo("Moving Forward")
            cmd_vel.publish(move_cmd)
            rospy.sleep(request.radius / 0.2)
            rospy.loginfo("Going Around")
            cmd_vel.publish(turn_cmd)
            rospy.sleep(1)
            count = count+1
    cmd_vel.publish(Twist())
    my_response.success = True
    return my_response

rospy.init_node('My_service')
cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=10)
move_cmd = Twist()
move_cmd.linear.x = 0.2
turn_cmd = Twist()
turn_cmd.linear.x = 0
turn_cmd.angular.z = radians(90)
multi_square_service = rospy.Service('/multi_square_service', MyServiceMsg, my_callback)
rospy.spin()
