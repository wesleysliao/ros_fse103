#!/usr/bin/env python

import sys
import rospy
from geometry_msgs.msg import Vector3

from python_fse103.fse103 import FSE103

def fse103node():
    argv = sys.argv
    rospy.myargv(argv)

    serialport_name = argv[1]
    publish_rate = argv[2]

    sensor = FSE103(serialport_name)

    pub = rospy.Publisher('FSE103/force', Vector3, queue_size=10)
    rospy.init_node('fse103_node', anonymous=True)
    rate = rospy.Rate(float(publish_rate))

    while not rospy.is_shutdown():
        sensor.read()
        pub.publish(sensor.force_x, sensor.force_y, sensor.force_z)
        rate.sleep()

if __name__ == '__main__':
    try:
        fse103node()
    except rospy.ROSInterruptException:
        pass