#!/usr/bin/env python

import sys
import rospy
from geometry_msgs.msg import Vector3, Wrench, WrenchStamped
from std_msgs.msg import Header

from python_fse103.fse103 import FSE103

def fse103node(serialport_name, publish_rate, frame_id):
    sensor = FSE103(serialport_name)

    pub = rospy.Publisher('fse103', WrenchStamped, queue_size=10)
    rospy.init_node('fse103_node', anonymous=True)
    rate = rospy.Rate(float(publish_rate))

    publishcount = 0

    while not rospy.is_shutdown():
        sensor.read()
        pub.publish(
            WrenchStamped(
                Header(
		    publishcount,
                    rospy.Time.now(),
                    frame_id),
                Wrench(
                    Vector3(sensor.force_x, sensor.force_y, sensor.force_z),
                    Vector3(0,0,0))))

        publishcount += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        argv = sys.argv
        rospy.myargv(argv)

        serialport_name = argv[1]
        publish_rate = argv[2]
        frame_id = argv[3]

        fse103node(serialport_name, publish_rate, frame_id)
    except rospy.ROSInterruptException:
        pass
