#! /usr/bin/env python

import rospy
import actionlib
from actionlib_tutorials.msg import FibonacciAction, FibonacciGoal, FibonacciFeedback, FibonacciResult

def callback(goal):
    r = rospy.Rate(2)
    success = True

    feedback.sequence = []
    feedback.sequence.append(1)
    #feedback.sequence.append(2)

    rospy.loginfo('%s: Executing, creating geometric sequence of order %i with seeds %i' % (action_server_name, goal.order, feedback.sequence[0]))

    for i in range(1, goal.order):
        if action_server.is_preempt_requested():
            rospy.loginfo('%s: Preempted' % action_server_name)
            action_server.set_preempted()
            success = False
            break
        feedback.sequence.append(feedback.sequence[i-1] * 2)
        action_server.publish_feedback(feedback)
        r.sleep()

    if success:
        result.sequence = feedback.sequence
        rospy.loginfo('%s: Succeeded' % action_server_name)
        action_server.set_succeeded(result)

rospy.init_node('geometric')
action_server = actionlib.SimpleActionServer("fibonacci_server", FibonacciAction, callback, auto_start = False)
action_server_name = "Fibonacci Action Server"
action_server.start()

feedback = FibonacciFeedback()
result = FibonacciResult()

rospy.spin()


