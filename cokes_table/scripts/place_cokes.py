#!/usr/bin/env python

import math, rospy
from utilities import pause_physics, unpause_physics, \
                      set_model_state
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_about_axis
from tf.transformations import quaternion_multiply
# *math.cos(math.radians(theta))
# *math.sin(math.radians(theta))
pause_physics()

for i in range(12):
    theta = i*360/12
    xp = 0.4 * math.cos(math.radians(theta)) + 1.0
    yp = 0.4 * math.sin(math.radians(theta)) + 0.0
    position = Point(x=xp, y=yp, z=1.1)


    q_z = quaternion_about_axis(math.radians(theta), (0,0,1))
    q_y = quaternion_about_axis(math.radians(90), (0,1,0))
    q_zy = quaternion_multiply(q_z, q_y)
    orientation = Quaternion(*q_zy)

    set_model_state('coke_can_' + str(i), Pose(position, orientation))
    rospy.sleep(0.5)
