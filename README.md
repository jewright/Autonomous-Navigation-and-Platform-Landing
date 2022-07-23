# Autonomous Navigation using a Jackal UGV
For furthering advancement toward autonomous navigation and platform landing, I implemented ROS onto robotic hardware and software. The ROS distribution used as melodic along with Ubuntu 18.04 on the Host PC used for this project.


## Hardware Used
For this project a variety of hardware and robotic accessories were used: 
- Host Ubuntu PC
- Vicon Motion Capture System
- Clearpath Robotics Jackal UGV
- UAV
- Point Grey Bumbleebee2 Stereo Vision Camera
- Hokuyo UST-10LX 2D LiDAR Sensor


## Vicon 

Vicon, a motion capture system, was utilized in the beginning of this project to learn position and localization. It provided the location of the Jackal UGV and UAV within the specified environment. 

![IMG_8583](https://user-images.githubusercontent.com/98404383/180620543-3a49abf8-dbef-47d9-b884-f273d11532b7.jpeg)


### Camera Calibration 
To begin the usage of Vicon, camera calibration is required. A wand provided for the system has flashing red LEDs and you must walk around and wave it until the cameras no longer blinks. You then must place the wand flat on the ground to set the origin of the environment.

![IMG_8652](https://user-images.githubusercontent.com/98404383/180620554-91ecd706-19f4-41d0-904d-86bfed7c094c.jpeg)


### Object Identification 
Object identification is an essential to provide an interaction between the Vicon system, Jackal UGV, and UAV. The Jackal and UAV both had reflective markers on top of them for the Vicon system to recognize and locate them in the environment. Within the Vicon tracker software, you're able to highlight over them and create new objects with their names assigned. This allows for the location data to be communicated when you launch scripts.  



### Scripts
For behavioral control of the UGV and UAV, Python, and ROS are used for programming implementations. The Jackal UGV and UAV both had ROS topics of the Vicon Motion Capture system. This was done with the usage ROS launch files. Once the location communication was set, I created and wrote several programs for different trajectories for the Vicon environment. Each program application provided a scenario for the UAV to land on the platform while in motion. 


## Jackal UGV
To further advance with autonomous Navigation, I began working with the Jackal UGV individually. The Vicon Motion Capture System allowed an understanding of the localization of objects; however, it was within a set environment. 

Before working with the physical Jackal, I created a simulation using Gazebo and Rviz on the host PC using ROS Melodic. Using Gazebo alongside RViz, I generated a unique map of the simulated room using the configuration of lidar sensors on a Jackal UGV. Utilizing multiple ROS tools, which included Navigation Stack, SLAM, Gmapping, Localization, and Visualization the map served as a guide for the testing and validation. 


### Hardware
The Jackal UGV used has an onboard computer that is fully integrated with ROS. Before working with physical Jackal’s accessories, I determine it was useful to  completely reset the Jackal’s OS. By setting everything to default, I was able to make it as configurable as I wanted. After these resetting changes, I connected a PS4 controller to manually control the Jackal and successfully confirmed  that everything was installed correctly in conjunction with the  default robot configurations. 


After confirming proper functionality, I added additional Accessories. This included a Point Grey Bumblebee2 and a Hokuyo UST-10LX. The Bumbleebee2 is a Stereo Vision Camera and the UST-10LX is a 2D LiDAR. After the proper network configuration of the host PC and Jackal, I was able to source the Jackal UGV to reflect its activity onto the PC. 





