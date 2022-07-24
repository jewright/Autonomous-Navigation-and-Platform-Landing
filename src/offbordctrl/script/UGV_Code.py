#!/usr/bin/env python

__author__ = 'Mushahid Rasul'

import rospy
import time
from geometry_msgs.msg import Twist, TransformStamped
from math import radians, sin, cos, degrees,  atan2
from nav_msgs.msg import Odometry
import numpy as np
import tf
from tf.transformations import euler_from_quaternion
from offbordctrl.msg import RequestFlag

class ugvControl():
    def __init__(self, ugv_num):
        self.pub = None
        self.X = np.zeros((1,2))
        self.x_data = []
        self.y_data = []
        self.start_x = 0
        self.start_y = 0
        self.yaw = 0 
        self.stopThread = False
        self.ugv_num = ugv_num
        self.last_yaw = 0 
        self.odomCheck = False
        self.radius = 0.5                         # Radius for Circle Trajectory
        self.circle = []
        self.squarex = []
        self.squarey = []
        self.X_pos =[]
        self.Y_pos =[]
        self.linearx = []
        self.lineary = []
    
        # self.Landing_Request_Received = False   # Request to land signal from UAV
        # self.UGV_Is_Occupied = False            # UGV initially Free to land on
        # self.clear_To_Land = False              # UGV sends clear_To_Land to land

        # self.setLanding_Request_Received = rospy.Publisher('UAV_Request', RequestFlag, queue_size=100)
        # self.setUGV_Is_Occupied = rospy.Publisher('UGV_Occupied', RequestFlag, queue_size=100)
        # self.setClear_To_Land = rospy.Publisher('UGV_Confirmation', RequestFlag, queue_size=100)

        self.pub  = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # rospy.Subscriber('/jackal'+str(self.ugv_num)+'/odometry/global_filtered', Odometry, self.odomRead)
        # rospy.Subscriber('UAV_Request', RequestFlag, self.UAV_Request)
        # rospy.Subscriber('UGV_Occupied', RequestFlag, self.UGV_Occupied)
        # rospy.Subscriber('UGV_Confirmation', RequestFlag, self.UGV_Confirmation)
        
        rospy.Subscriber('/vicon/jackal'+str(self.ugv_num)+'/jackal'+str(self.ugv_num), TransformStamped, self.jackle2_cb)
        
    def jackle2_cb(self, msg):
      x = msg.transform.translation.x
      y = msg.transform.translation.y
      self.x_data.append(x)
      self.y_data.append(y)
      orientation_list = [msg.transform.rotation.x, msg.transform.rotation.y, msg.transform.rotation.z, msg.transform.rotation.w]
      (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
      self.X[0,0] = x 
      self.X[0,1] = y
      self.yaw = degrees(yaw)
      self.odomCheck = True   

    # def odomRead(self,msg):
    #     x = msg.pose.pose.position.x
    #     y = msg.pose.pose.position.y
    #     z = msg.pose.pose.position.z
    #     self.X[0,0] = x 
    #     self.X[0,1] = y
    #     self.x_data.append(x)
    #     self.y_data.append(y)
    #     self.z_data.append(z)
    #     orientation_list = [msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w]
    #     (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    #     self.yaw = degrees(yaw)
    #     self.odomCheck = True

    def move(self,pub,x,y,z):
        twist = Twist()
        speed = 0.3  
        twist.linear.x = x*speed 
        twist.linear.y = y*speed
        twist.linear.z = z*speed
        twist.angular.x = 0 
        twist.angular.y = 0 
        twist.angular.z = 0
        pub.publish(twist)

    def rotate(self,pub,deg,leftorright):
        twist = Twist()
        speed = 0.3  
        twist.linear.x = 0
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0 
        twist.angular.y = 0 
        if leftorright:
            twist.angular.z = speed
        else:
            twist.angular.z = -speed
        self.last_yaw = self.yaw
        rate = rospy.Rate(10.0)
        self.move(pub,0,0,0)
        while abs(self.yaw-self.last_yaw) < deg and not self.stopThread:
            pub.publish(twist)
            rate.sleep()
        self.move(pub,0,0,0) 
        

    def rotateZero(self,pub):
        rate = rospy.Rate(10.0)
        twist = Twist()
        speed = 0.3  
        twist.linear.x = 0
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0 
        twist.angular.y = 0 
        if yaw>0:
            twist.angular.z = -speed
        else:
            twist.angular.z = speed
          
        self.move(pub,0,0,0)
        while abs(self.yaw) > 2 and not self.stopThread:
            pub.publish(twist)
            rate.sleep()
        self.move(pub,0,0,0)

    def rotateabsoluteAngle(self,pub,ang):
        rate = rospy.Rate(10.0)
        twist = Twist()
        speed = 0.3  
        twist.linear.x = 0
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0 
        twist.angular.y = 0 

        dl = ang - self.yaw
        # dl = dl - 90
        if (ang >=0 and self.yaw >=0) or (ang < 0 and self.yaw < 0):

            if dl >= 0: 
                twist.angular.z = speed  # CCW
            else:
                twist.angular.z = -speed # CW

        elif (ang >=0 and self.yaw <=0):
            if dl <= 180: 
                twist.angular.z = speed  # CCW
            else:
                twist.angular.z = -speed # CW

        elif (ang <= 0 and self.yaw >=0):
            if dl <= -180: 
                twist.angular.z = speed  # CCW
            else:
                twist.angular.z = -speed # CW
        
        
        self.move(pub,0,0,0)

        while abs(ang-self.yaw) > 2 and not self.stopThread:
            pub.publish(twist)
            rate.sleep()
        self.move(pub,0,0,0) 

    def goto_2dLocation(self,pub,x,y,callback=None):
                #calculate desired angle
        dx = x-self.X[0,0]
        dy = y-self.X[0,1]

        dang = degrees(atan2(dy,dx))
        self.rotateabsoluteAngle(pub,dang)
        
        velError = np.hypot(dx,dy)
        angleError = dang-self.yaw

        rate = rospy.Rate(10) #10
        twist = Twist()
        speed = 0.3 #0.3 m/s
        twist.linear.x = 0.7 #0.3
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0 
        twist.angular.y = 0
        twist.angular.z = 0
        kp_ang = 0.009 #0.05
        kp_dis = 0.1 #0.1
        counter = 0
        
        while velError >= 0.43 and counter<800 and not self.stopThread: #0.15 300 1.1 1.3(L)
            # print("IN THE LOOP")
            # if callback is not None:
            #     checkCallback()   
            dx = x-self.X[0,0]
            dy = y-self.X[0,1]
            velError = np.hypot(dx,dy)
            print("current: ", self.X[0,0],self.X[0,1])
            print("Goingto: ", x,y)
            print("Error: ", velError)
            twist.linear.x = max(min(kp_dis*velError, speed),0.7) #0.3, 0.2
            twist.angular.z = min(kp_ang*angleError, 0.1)
            pub.publish(twist)
            rate.sleep()
            counter += 1
        self.move(pub,0,0,0)
      
##########################################################################################
    # def UAV_Request(self,msg):
    #     print("UAV:"+str(msg.frame_id)+" Request Received: "+ str(self.Landing_Request_Received))
    #     if  self.UGV_Is_Occupied == False and msg.data == True:
    #         msg.data = True
    #         self.UGV_Is_Occupied = True
    #         self.setClear_To_Land.publish(msg)
        
    # def UGV_Occupied(self,msg):
    #     self.UGV_Is_Occupied = msg.data
    #     print("UGV is Occupied: ", self.UGV_Is_Occupied)
    #     self.setUGV_Is_Occupied.publish(msg)

    # def UGV_Confirmation(self,msg):  
    #     self.clear_To_Land = msg.data
    #     print("UAV:"+str(msg.frame_id)+" CLEAR TO LAND: "+ str(self.clear_To_Land))

##########################################################################################
    # def checkCallback(self):
    #     if self.Landing_Request_Received == True and self.UGV_Is_Occupied == False:
    #         self.clear_To_Land = True
    #         self.UGV_Is_Occupied = True
    #         self.setClear_To_Land.publish(self.clear_To_Land)

# Linear Trajectory
    def Linear_Traj(self):  
        self.linearx = [2,-0.4]
        self.lineary = [3,3]

        while True:
            for i in range(len(self.linearx)):
                self.X_pos.append(self.linearx[i])
                self.Y_pos.append(self.lineary[i]) 
                self.goto_2dLocation(self.pub,self.X_pos[i],self.Y_pos[i])
            if True:
                break   
        rospy.sleep(1)
        print("Linear Completed")  

# Square Trajectory
    def Sqaure_Traj(self): 
        self.squarex = [2,2,-0.4,-0.4,1]
        self.squarey = [3,6,   6,   3,3]

        while True:
            for i in range(len(self.squarex)):
                self.X_pos.append(self.squarex[i])
                self.Y_pos.append(self.squarey[i]) 
                self.goto_2dLocation(self.pub,self.X_pos[i],self.Y_pos[i])
            if True:
                break   
        rospy.sleep(1)
        print("Square Completed")   

# Circle Trajectory
    def Circle_Traj(self): 
    
        self.circle = np.linspace(0,360,10) 

    # Get the initial location.
        self.start_x = self.X[0,0]
        self.start_y = self.X[0,1]
        # print(self.start_x, self.start_y)
        # print(self.X[0,0], self.X[0,1])
        rate = rospy.Rate(10) #10
        twist = Twist()
        speed = 0.4 #0.3 m/s
        twist.linear.x = 0.3 #0.3
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0 
        twist.angular.y = 0
        twist.angular.z = 0
        kp_ang = 0.5 #0.05
        kp_dis = 0.1 #0.1
        
        while True:
            for _ in range(2500):
                twist.linear.x = 0.35
                twist.angular.z = 0.3
                self.pub.publish(twist)
                rate.sleep()
                if self.stopThread:
                    break
            # for theta in self.circle:
            #     x=self.start_x+cos(radians(theta))*self.radius
            #     y=self.start_y+sin(radians(theta))*self.radius

            #     dx = x-self.X[0,0]
            #     dy = y-self.X[0,1]
            #     velError = np.hypot(dx, dy)
            #     dang = theta 
            #     angleError = (dang-self.yaw)
            #     counter = 0
                
            #     while (velError >= 0.2 or angleError >= 5.0) and counter<15 and not self.stopThread: #0.2 5.0
            #         # if callback is not None:
            #         #     checkCallback()   
            #         dx = x-self.X[0,0]
            #         dy = y-self.X[0,1]
            #         velError = np.hypot(dx, dy)
            #         if self.yaw < 0:
            #             self.yaw += 360

            #         angleError = min(abs((dang-self.yaw)), abs((dang + 360 - self.yaw)))
            #         twist.linear.x = max(min(kp_dis*velError, speed),0.35) #0.35
            #         twist.angular.z = min(kp_ang*angleError, 0.3) #0.3
            #         print("Linear_X: ", twist.linear.x)
            #         print("Angular_Z: ", twist.angular.z)
            #         self.pub.publish(twist)
            #         rate.sleep()
            #         counter += 1

            #     print(velError,angleError)
            if True:
                break
        rospy.sleep(1)
        print("Circle Completed")  

    def loop(self):
        while not self.odomCheck:
            rospy.sleep(1)
        rate = rospy.Rate(20.0) 
       
        # Different Scenarios, Uncomment to simulate.

        #self.Linear_Traj()
        # self.Sqaure_Traj()
        self.Circle_Traj()
  