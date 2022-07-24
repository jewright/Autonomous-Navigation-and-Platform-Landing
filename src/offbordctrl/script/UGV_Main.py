#!/usr/bin/env python

import rospy
import threading
from UGV_Code import ugvControl

if __name__ == '__main__':          
    try:
        rospy.init_node('UGV_Main', anonymous=True)


        ugv = ugvControl(ugv_num=2)
        threading.Thread(target=ugv.loop).start()
            
        rate = rospy.Rate(5.0)
        while not rospy.is_shutdown():
          rate.sleep()
          cmd = raw_input("command: \"l\" to stop the UGV and \"q\" for exit the main loop: ")
 
          if cmd=='l':
            ugv.stopThread = True
          elif cmd=='q':
            ugv.stopThread = True
            rospy.sleep(5)
            break

    except rospy.ROSInterruptException:
        pass
 