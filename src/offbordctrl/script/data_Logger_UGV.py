#!/usr/bin/env python
__author__ = 'Mushahid Rasul'
# This Program Logs all sensory data for the Jackal.
# JACKALS POSITION and VELOCITY

import rospy
from geometry_msgs.msg import TransformStamped
import threading
from nav_msgs.msg import Odometry
import pandas as pd
import csv

class UGV_logger():
    def __init__(self):
        self.time = 0
        self.Jackal_X_pos = 0
        self.Jackal_Y_pos = 0
        self.Jackal_Z_pos = 0
        self.Jackal_X_vel = 0
        self.Jackal_Y_vel = 0
        self.Jackal_Z_vel = 0
        self.stop = False
        self.counter = 0
        rospy.Subscriber('/odometry/filtered', Odometry, self.current_vel)
        rospy.Subscriber('/vicon/jackal2/jackal2', TransformStamped, self.jackle2_cb)


    def current_vel(self,msg):
        self.Jackal_X_vel = msg.twist.twist.linear.x
        self.Jackal_Y_vel = msg.twist.twist.linear.y
        self.Jackal_Z_vel = msg.twist.twist.linear.z
        self.counter = 1
    
    def jackle2_cb(self, msg):
        self.time = msg.header.stamp.secs
        self.Jackal_X_pos = msg.transform.translation.x
        self.Jackal_Y_pos = msg.transform.translation.y
        self.Jackal_Z_pos = msg.transform.translation.z
        self.counter += 1

    def loop(self):
        time_data = []
        Jackal_xVel = []
        Jackal_yVel = []
        Jackal_zVel = []
        Jackal_xPos = []
        Jackal_yPos = []
        Jackal_zPos = []

        rate = rospy.Rate(60.0)
        while not self.stop:
            if self.counter >= 2:
                time_data.append(self.time)
                Jackal_xVel.append(self.Jackal_X_vel)
                Jackal_yVel.append(self.Jackal_Y_vel)
                Jackal_zVel.append(self.Jackal_Z_vel)
                Jackal_xPos.append(self.Jackal_X_pos)
                Jackal_yPos.append(self.Jackal_Y_pos)
                Jackal_zPos.append(self.Jackal_Z_pos)
                rate.sleep()


        data = {'time':time_data,'X_Vel':Jackal_xVel,'Y_Vel':Jackal_yVel,'Z_Vel':Jackal_zVel,
                'X_POS':Jackal_xPos,'Y_POS':Jackal_yPos,'Z_POS':Jackal_zPos}
        df = pd.DataFrame(data=data)

        fileName = "/home/administrator/ros-intel-uav-rpeo/jackal2_ws/src/offbordctrl/script/data_log/trial_6.csv"
        df.to_csv(fileName,index=False)

if __name__ == '__main__':          
    try:
        rospy.init_node('data_Logger_UGV', anonymous=True)
        log = UGV_logger()
        threading.Thread(target=log.loop).start()
        rospy.sleep(5)

        while not rospy.is_shutdown():

            cmd = raw_input("command: \"q\" exit program: ")
            if cmd=='q':
                log.stop = True
                rospy.sleep(15)
                break

    except rospy.ROSInterruptException:
        pass  
   