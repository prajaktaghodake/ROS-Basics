#! /usr/bin/env python

import rospy
import actionlib
from ex12_turtle_as.msg import MoveAction, MoveGoal, MoveFeedback, MoveResult

def callback(feedback):
    print('Feedback received: ')
    print(feedback)

rospy.init_node('turtle_action_client')

client = actionlib.SimpleActionClient('/turtle_server', MoveAction)
client.wait_for_server()

goal = MoveGoal()
goal.duration = 10
goal.direction = "FORWARD"


client.send_goal(goal, feedback_cb = callback)

rospy.sleep(4)
client.cancel_goal()

client.wait_for_result()
state_result = client.get_state()

print('[Result] State: %d' %state_result)
#while state_result < 2:
    #rospy.loginfo("Doing other stuff while the action server does its thing...")
    #state_result = client.get_state()
    #rospy.sleep(1)


