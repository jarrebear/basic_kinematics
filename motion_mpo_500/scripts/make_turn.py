#! /usr/bin/env python

import rospy, math, numpy as np
from std_msgs.msg import Float32MultiArray
from utilities import reset_world

def twist2wheels(wz, vx, vy):
    v_array = np.array([wz, vx, vy])
    l = .500/2
    w = .548/2
    r = .254/2
    H = np.array([[-l-w, 1, -1], [l+w, 1, 1], [l+w, 1, -1], [-l-w, 1, 1]])

    u = np.dot(H, v_array) / r

    return u.flatten().tolist()

rospy.init_node('make_turn', anonymous=True)
pub = rospy.Publisher('wheel_speed', Float32MultiArray, queue_size=10)
rospy.sleep(1)

u = twist2wheels(wz=1.5, vx=1, vy=0)
msg = Float32MultiArray(data=u)
pub.publish(msg)
rospy.sleep(1)
stop = [0,0,0,0]
msg = Float32MultiArray(data=stop)
pub.publish(msg)