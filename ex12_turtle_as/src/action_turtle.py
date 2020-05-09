#! /usr/bin/env python

import rospy
import actionlib
from ex12_turtle_as.msg import MoveAction, MoveGoal, MoveFeedback, MoveResult
from geometry_msgs.msg import Twist

def callback(goal):
    r = rospy.Rate(2)
    success = True
    vel=Twist()
    

    #rospy.loginfo('%s: Executing, creating fibonacci sequence of order %i with seeds %i' % (action_server_name, goal.order, feedback.sequence[0]))
    
    for i in range(1, goal.duration):
        if action_server.is_preempt_requested():
            rospy.loginfo('%s: Preempted' % action_server_name)
            action_server.set_preempted()
            success = False
            break
        if goal.direction == "FORWARD":
            vel.linear.x= 0.2
            vel_pub.publish(vel)
            i+=1
            feedback.current_state= "Moving forward!"
            action_server.publish_feedback(feedback)
            r.sleep()
        elif goal.direction == "BACKWARD":
            vel.linear.x= -0.2
            i+=1
            vel_pub.publish(vel)
            feedback.current_state="Moving Backward!"
            action_server.publish_feedback(feedback)
            r.sleep()
        else:
            rospy.loginfo('%s: Incorrect goal: Please specify FORWARD or BACKWARD!' % (goal.direction))
    if success:
        result.final_state = "Finished moving!"
        rospy.loginfo('%s: Succeeded' % action_server_name)
        action_server.set_succeeded(result)

    vel.linear.x=0
    vel_pub.publish(vel)

rospy.init_node('turtle')
vel_pub=rospy.Publisher("cmd_vel", Twist, queue_size=1)
action_server = actionlib.SimpleActionServer("turtle_server", MoveAction, callback, auto_start = False)
action_server_name = "Turtle Action Server"
action_server.start()

feedback = MoveFeedback()
result = MoveResult()

rospy.spin()

