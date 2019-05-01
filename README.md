# ros_fse103
ROS Package for the Varience FSE103 force sensor, implemented in python.

## Usage:
`rosrun ros_fse103 fse103_node.py [serialport] [publishrate] [frame_id]`

Replace `[serialport]` with your serial port device, `[publishrate]` with how fast you want data published, and `[frame_id]` with the frame you want the Wrench to be relative to.

### Example:

To read from an FSE103 on /dev/ttyACM0 at 10Hz in the "force_sensor" frame:

`rosrun ros_fse103 fse103_node.py /dev/ttyACM0 10 force_sensor`

Data is published as a geometry_msgs/WrenchStamped on "fse103"
