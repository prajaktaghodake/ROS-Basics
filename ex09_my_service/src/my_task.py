#! /usr/bin/env python
import rospy
from std_srvs.srv import Empty, EmptyResponse 
from move_square import MoveBB8

def my_callback(request):

    rospy.loginfo("The Service has been called")
    robot_object = MoveBB8()
    robot_object.move_square()
    rospy.loginfo("Finished the Service which has been called")
    return EmptyResponse()

rospy.init_node('service_move_robot_square_server')
my_service = rospy.Service('/my_service', Empty , my_callback)
rospy.loginfo("Service is ready")
rospy.spin()
