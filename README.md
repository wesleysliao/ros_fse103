# ros_fse103
ROS Package for the Varience FSE103 force sensor, implemented in python.

## Usage:
`rosrun ros_fse103 fse103_node.py [serialport] [publishrate]`

Replace `[serialport]` with your serial port device and `[publishrate]` with how fast you want data published.

### Example:

To read from an FSE103 on /dev/ttyACM0 at 10Hz:

`rosrun ros_fse103 fse103_node.py /dev/ttyACM0 10`

Data is published as a geometry_msgs/Vector3 on FSE103/force
