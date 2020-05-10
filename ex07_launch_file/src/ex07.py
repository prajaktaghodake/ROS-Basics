#!/usr/bin/env python

import rospy
from goal_publisher.msg import PointArray

def callback(msg):
    i=0
    while (i<20):
        #print(".*Point0 : x: ={a}, y:={b} ,z:={c}".format(a= msg.goals[i].x,b= msg.goals[i].y,c= msg.goals[i].z))
        #print(".*Point1 : x: ={d}, y:={e} ,z:={f}".format(d= msg.goals[i].x+1,e=msg.goals[i].y+1,f=msg.goals[i].z))
        #print(".*Point2 : x: ={g}, y:={h} ,z:={i}".format(g= msg.goals[i].x +2,h=msg.goals[i].y+2,i=msg.goals[i].z))
        print("Point: {%0.2f}".format(msg.goals[i].x))
        i=i+1

rospy.init_node('goal_launch')
rospy.Subscriber('/points', PointArray, callback)
rospy.spin()
