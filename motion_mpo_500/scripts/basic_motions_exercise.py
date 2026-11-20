#! /usr/bin/env python

import rospy, math, numpy as np
from std_msgs.msg import Float32MultiArray
from utilities import reset_world

rospy.init_node('holonomic_controller', anonymous=True)
pub = rospy.Publisher('wheel_speed', Float32MultiArray, queue_size=10)
rospy.sleep(1.0)

backwards = [-1, -1, -1, -1]
msg = Float32MultiArray(data=backwards)
pub.publish(msg)

rospy.sleep(1.0)

left = [-1, 1, -1, 1]
msg = Float32MultiArray(data=left)
pub.publish(msg)

rospy.sleep(1.0)

right = [1, -1, 1, -1]
msg = Float32MultiArray(data=right)
pub.publish(msg)

rospy.sleep(1.0)

#clockwise
rotations_cw = [1, -1, -1, 1]
msg = Float32MultiArray(data=rotations_cw)
pub.publish(msg)

rospy.sleep(1.0)

#counterclockwise
rotations_ccw = [-1, 1, 1, -1]
msg = Float32MultiArray(data=rotations_ccw)
pub.publish(msg)

rospy.sleep(1.0)

stop = [0, 0, 0, 0]
msg = Float32MultiArray(data=stop)
pub.publish(msg)