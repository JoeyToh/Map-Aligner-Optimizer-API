#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

class MapAlignerPublisher():
    def __init__(self):
        pass

    def publish(self):
        pub = rospy.Publisher('map_aligner', Bool, queue_size=10)
        rospy.init_node('map_aligner_publisher', anonymous=True)
        rospy.sleep(1)
        bool = True
        rospy.loginfo(bool)
        pub.publish(bool)

if __name__ == '__main__':
    try:
        connector = MapAlignerPublisher()
    except rospy.ROSInterruptException:
        pass