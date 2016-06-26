#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple sensor demo that published std_msgs/Strings messages
## to the 'chatter' topic

from math import pi

import rospy
from sensor_msgs.msg import JointState

from adc_utilities import * 
from utilities import *

from geometry_msgs.msg import Quaternion

def sensor():
    import sys
    print(sys.version)

    pub = rospy.Publisher('JointState', JointState, queue_size=10)
    rospy.init_node('StringPotSensor', anonymous=True)
    rate = rospy.Rate(100) # 100hz
    while not rospy.is_shutdown():
        rawStringPot = readAin(AIN4, KNEE_RANGE)
        rospy.loginfo(rawStringPot)
	
        radianAngle = strPot_to_angle(rawStringPot, KNEE_POT_RANGE, KNEE_PISTON_RANGE, KNEE_OFFSETS)
        rospy.loginfo(radianAngle)
        
        msg = JointState() 
        msg.position = radianAngle
        pub.publish(msg)
        rate.sleep()

# Values pulled from Solidworks
KNEE_POT_RANGE = (148, 934)
KNEE_PISTON_RANGE = (20,32)
KNEE_OFFSETS = (25.602, 7.439)
THIGH_POT_RANGE = (93, 723)
THIGH_PISTON_RANGE = (24,38)
THIGH_OFFSETS = (10.216, 33.431)


if __name__ == '__main__':
    try:
        sensor()
    except rospy.ROSInterruptException:
        pass
