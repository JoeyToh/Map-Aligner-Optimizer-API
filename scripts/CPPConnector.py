#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

class CPPConnector():
    def __init__(self):
        self.talker()

    def talker(self):
        pub = rospy.Publisher('chatter', Bool, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        rospy.sleep(1)
        bool = True
        rospy.loginfo(bool)
        pub.publish(bool)

if __name__ == '__main__':
    try:
        connector = CPPConnector()
    except rospy.ROSInterruptException:
        pass