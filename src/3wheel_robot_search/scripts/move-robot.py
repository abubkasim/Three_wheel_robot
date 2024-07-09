#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def move_robot(path):
    rospy.loginfo("Moving robot along path: %s", path.data)
    # Implement movement logic here

def move_node():
    rospy.init_node('move_node', anonymous=True)
    rospy.Subscriber('/robot_path', String, move_robot)
    rospy.spin()

if __name__ == '__main__':
    try:
        move_node()
    except rospy.ROSInterruptException:
        pass

