# Created By Jordyn Wright

# Imports
import rospy
import time
from geometry_msgs.msg import Twist, TransformStamped
from math import radians, sin, cos, degrees, atan2
from nav_msgs.msg import Odometry
import numpy as np
import tf
from tf.transformations import euler_from_quaternion
from offbordctrl.msg import RequestFlag
import yaml
import multiprocessing

class ugvControl():
    def __init__(self, ugv_num):
        self.pub = None
        self.X = np.zeros((1, 2))
        self.x_data = []
        self.y_data = []
        self.start_x = 0
        self.start_y = 0
        self.yaw = 0
        self.stopThread = False
        self.ugv_num = ugv_num
        self.last_yaw = 0
        self.odomCheck = False
        self.radius = 0.5  # Radius for Circle Trajectory
        self.circle = []
        self.squarex = []
        self.squarey = []
        self.X_pos = []
        self.Y_pos = []
        self.B_pos = []
        self.linearx = []
        self.lineary = []
        self.ptpx = []
        self.ptpy = []
        self.boundx = []
        self.boundy = []
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/vicon/jackal' + str(self.ugv_num) + '/jackal' +
                        str(self.ugv_num), TransformStamped, self.jackle2_cb)

    def jackle2_cb(self, msg):
        x = msg.transform.translation.x
        y = msg.transform.translation.y
        self.x_data.append(x)
        self.y_data.append(y)
        orientation_list = [msg.transform.rotation.x, msg.transform.rotation.y,
                            msg.transform.rotation.z, msg.transform.rotation.w]
        (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
        self.X[0, 0] = x
        self.X[0, 1] = y
        self.yaw = degrees(yaw)
        self.odomCheck = True

    def move(self, pub, x, y, z):
        twist = Twist()
        speed = 0.3
        twist.linear.x = x * speed
        twist.linear.y = y * speed
        twist.linear.z = z * speed
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
        speed = 0.1 #0.3 m/s
        twist.linear.x = 0.5 #0.3
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


    # Linear / Straight Line function
    def Linear(self):
        # Starting position
        self.start_x = self.X[0, 0]
        self.start_y = self.X[0, 1]
        # Define Twist
        twist = Twist()
        # Define speed and direction.
        # Speed = 0.3 m/s in a straight line
        speed = 0.3
        twist.linear.x = 0.3
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0
        # Timer so that the jackal will stop in 5 seconds
        timer = time.time() + 5
        # Jackal will move until the timer runs out
        while (time.time() < timer) :
            for i in range(2500):
                twist.linear.x = 0.35
                self.pub.publish(twist)
        # Message to indicate that the code has completed
        rospy.sleep(1)
        print("Linear Completed")

    def PointToPoint(self):
         
        self.ptpx = [1 , 1 ]
        self.ptpy = [1.5 , 2.5 ]

        
        while True:
            for i in range(len(self.ptpx)):
                self.X_pos.append(self.ptpx[i])
                self.Y_pos.append(self.ptpy[i]) 
                self.goto_2dLocation(self.pub,self.X_pos[i],self.Y_pos[i])
            if True:
                break   
        rospy.sleep(1)
        print("Completed")   

    def Square(self):
         
        self.squarex = [1.9 , 1.9 , 0.1 , 0.1 , 1.9 ]
        self.squarey = [1.5 , 3.5 , 3.5 , 1.5 , 1.5]

        
        while True:
            for i in range(len(self.squarex)):
                self.X_pos.append(self.squarex[i])
                self.Y_pos.append(self.squarey[i]) 
                self.goto_2dLocation(self.pub,self.X_pos[i],self.Y_pos[i])
            if True:
                break   
        rospy.sleep(1)
        print("Completed")   

    def Boundary(self):
        self.ptpx = [1 , 1 , 1 ]
        self.ptpy = [1.5 , 3.5 , 5 ]

        timer = time.time() + 10
        while (time.time() < timer):    
            for i in range(len(self.ptpx)):
                self.X_pos.append(self.ptpx[i])
                self.Y_pos.append(self.ptpy[i])
                while ((0.5 < self.ptpx[i] < 2) & (0.5 < self.ptpy[i] < 4)):
                    self.goto_2dLocation(self.pub,self.X_pos[i],self.Y_pos[i]),self.X_pos.append(self.ptpx[i])
                
            if True:
                break   
        rospy.sleep(1)
        print("Completed")  

    def loop(self):
        while not self.odomCheck:
            rospy.sleep(1)
            rate = rospy.Rate(20.0)
        
        # Different Scenarios
        # self.Linear()
        self.PointToPoint()
        # self.Square()
        # self.Boundary()

# Created By Jordyn Wright
