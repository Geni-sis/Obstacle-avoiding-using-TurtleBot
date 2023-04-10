#! /usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

pub = None
thresh=0.25

def clbk_laser(msg):
    regions = {
        '1':round(min(msg.ranges[0:44]),3),
        '2':round(min(msg.ranges[45:89]),3),
        '3':round(min(msg.ranges[90:134]),3),
        '4':round(min(msg.ranges[135:179]),3),
        '5':round(min(msg.ranges[180:224]),3),
        '6':round(min(msg.ranges[225:269]),3), 
        '7':round(min(msg.ranges[270:314]),3),
        '8':round(min(msg.ranges[315:360]),3),
    }
    take_action(regions)

def take_action(regions):
    msg = Twist()
    linear_x = 0
    angular_z = 0

    state_description = ''

    if regions['1'] > thresh and regions['2'] > thresh and regions['7'] > thresh and regions['8'] > thresh:
        state_description = 'case 1 - nothing'
        linear_x = 0.2
        angular_z = 0
    elif regions['1'] < thresh and regions['2'] > thresh and regions['7'] > thresh and regions['8'] < thresh:
        state_description = 'case 2 - front'
        linear_x = 0
        angular_z = -0.15
    elif regions['1'] < thresh and regions['7'] > thresh and regions['2'] < thresh and regions['8'] < thresh:
        state_description = 'case 6 - front and fleft'
        linear_x = 0
        angular_z = -0.15
    elif regions['8'] > thresh and regions['7'] > thresh and regions['2'] < thresh and regions['1'] < thresh:
        state_description = 'case 4 - fleft'
        linear_x = 0
        angular_z = -0.15
    elif regions['1'] > thresh and regions['3'] < thresh and regions['2'] < thresh and regions['8'] > thresh:
        state_description = 'case 2 - left'
        linear_x = 0.12
        angular_z = 0.315
    elif regions['1'] > thresh and regions['3'] < thresh and regions['4'] < thresh and regions['8'] > thresh:
        state_description = 'case 2 - back left'
        linear_x = 0
        angular_z = 0.15
    elif regions['8'] < thresh and regions['7'] < thresh and regions['2'] > thresh and regions['1'] > thresh:
        state_description = 'case 3 - fright'
        linear_x = 0
        angular_z = -0.15
    elif regions['1'] < thresh and regions['7'] < thresh and regions['2'] > thresh and regions['8'] < thresh:
        state_description = 'case 5 - front and fright'
        linear_x = 0
        angular_z = -0.15
    elif regions['1'] < thresh and regions['2'] < thresh and regions['7'] < thresh and regions['8'] < thresh:
        state_description = 'case 7 - front and fleft and fright'
        linear_x = 0
        angular_z = -0.15
    elif regions['1'] > thresh and regions['2'] < thresh and regions['7'] < thresh and regions['8'] > thresh:
        state_description = 'case 8 - fleft and fright'
        linear_x = 0
        angular_z = -0.15
    else:
        state_description = 'unknown case'
        linear_x=0.6
        angular_z=0
        rospy.loginfo(regions)

    rospy.loginfo(state_description)
    msg.linear.x = linear_x
    msg.angular.z = angular_z
    pub.publish(msg)


def main():
    global pub

    rospy.init_node('reading_laser')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    sub = rospy.Subscriber('/scan', LaserScan, clbk_laser)

    rospy.spin()

if __name__ == '__main__':
    main()