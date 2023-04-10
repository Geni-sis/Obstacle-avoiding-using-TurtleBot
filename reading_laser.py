#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

#360 points, 360/8=45
def clbk_Laser(msg):
    regions=[
        round(min(msg.ranges[0:44]),3),
        round(min(msg.ranges[45:89]),3),
        round(min(msg.ranges[90:134]),3),
        round(min(msg.ranges[135:179]),3),
        round(min(msg.ranges[180:224]),3),
        round(min(msg.ranges[225:269]),3), 
        round(min(msg.ranges[270:314]),3),
        round(min(msg.ranges[315:360]),3),
    ]
    rospy.loginfo(regions)  

def main():
    rospy.init_node('reading_laser')
    sub=rospy.Subscriber('/scan',LaserScan,clbk_Laser)
    print("1")
    rospy.spin()


if __name__=='__main__':
    main()