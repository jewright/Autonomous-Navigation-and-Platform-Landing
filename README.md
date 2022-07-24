# Autonomous Navigation and Platform Landing
This project is to further advancements in autonomous navigation and platform landing. Using ROS, I programmed robotic hardware and software. The ROS distribution used was melodic along with Ubuntu 18.04. Additionally, I used a UGV, UAV, and a Motion Capture system.                                                                                               


## Hardware Used
This project used a variety of hardware and robotic accessories: 
- Host Ubuntu PC
- Vicon Motion Capture System
- Clearpath Robotics Jackal UGV
- UAV
- Point Grey Bumbleebee2 Stereo Vision Camera
- Hokuyo UST-10LX 2D LiDAR Sensor


## Vicon 

Vicon, a motion capture system, was utilized at the beginning of this project to learn position and localization. It provided the location of the Jackal UGV and UAV within the specified environment. 

### Camera Calibration 
Vicon requires camera calibration for use. A wand provided for the system has flashing red LEDs. You must then walk around and wave it until the cameras no longer blink. You then must place the wand flat on the ground to set the origin of the environment.
<p align="center">
  <img width="300"  alt="CameraCalibrationWand" src="https://user-images.githubusercontent.com/98404383/180650846-1d45d3f8-39f3-4104-a94e-0d3e42091bd6.png"
  
</p>

### Object Identification 
Object identification is essential to provide an interaction between the Vicon system, Jackal UGV, and UAV. The Jackal and UAV had reflective markers on top for the Vicon system to recognize and locate them in the environment. Within the Vicon Tracker software, you create new objects then the location data can communicate when you launch scripts.  


![IMG_8648](https://user-images.githubusercontent.com/98404383/180620686-0ae67176-34ef-4a5e-9fc4-4a7e92de694d.JPG)


### Scripts
Using ROS and Python, I created programs to control the behavior of the UGV and UAV. They both had  ROS topics of the Vicon Motion Capture system with the usage of ROS launch files. Using the location data, I created and wrote several programs for different trajectories for the Vicon environment. Each program application provided a scenario for the UAV to land on the platform while in motion. 



https://user-images.githubusercontent.com/98404383/180629362-b7529f71-5982-4102-8732-fd885f3d8a86.mp4




## Using Jackal UGV for Autonomous Navigation 
Working individually with the Jackal UGV, I was able to advance autonomous navigation. While the Vicon Motion Capture System allowed an understanding of the localization of objects, it was within a set environment. 


### Simulation
Before working with the physical Jackal, I created a simulation using Gazebo and Rviz on the host PC using ROS Melodic. Using Gazebo alongside RViz, I generated a unique map of the simulated room using the configuration of lidar sensors on a Jackal UGV. Utilizing multiple ROS tools, which included navigation stack, SLAM, gmapping, localization, and visualization, the map served as a guide for the testing and validation. 


<img width="600" alt="SimulationMap" src="https://user-images.githubusercontent.com/98404383/180628936-ef11a5c6-ed48-4cbc-bbfe-c99b213a7054.png">



### Hardware
The Jackal UGV used has an onboard computer fully integrated with ROS. Before working with physical Jackal’s accessories, I determined it was best to reset Jackal’s operating system. By setting everything to default, I could make it as configurable as I wanted. After these resetting changes, I connected a PS4 controller for manual control. 


![IMG_8574](https://user-images.githubusercontent.com/98404383/180629410-eeb4ef37-c50d-4bf4-a994-60cd93fb1679.png)


After confirming proper functionality, I added additional Accessories. The Jackal had two accessories, a Point Grey Bumblebee2 (Stereo Vision Camera) and a Hokuyo UST-10LX (2D LiDAR). After the proper network configuration of the host PC and Jackal, I sourced the Jackal UGV to reflect its activity onto the PC. I could see everything the Jackal UGV was doing through software such as RViz, RQT robot monitor, and Raw Image streams. 


https://user-images.githubusercontent.com/98404383/180629384-1bc176bd-ec11-4c7b-8740-de0aecf23989.mp4
