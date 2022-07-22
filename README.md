# Autonomous Navigation using a Jackal UGV
For furthering advancement toward autonomous navigation and platform landing, I implemented ROS onto robotic hardware and software. The ROS distribution used as melodic along with Ubuntu 18.04 on the Host PC used for this project.

## Hardware Used
For this project a variety of hardware and robotic accessories were used: 
- Host Ubuntu PC
- Vicon Motion Capture System
- Clearpath Robotics JAckal UGV
- UAV
- Point Grey Bumbleebee2 Stereo Vision Camera
- Hokuyo UST-10LX 2D LiDAR Sensor


## Vicon 



Vicon, a motion capture system, was utilized in the beggining of this project to learn position and localization.It was capable and provided the location of the JAckal UGV and UAV within the specified environment. The Vicon system requires camera calibration and object identification to work alongside the Jackal UGV and the UAV. 

### Camera Calibration 
To begin the usage of Vicon, the cameras must be calibrated. A wand provided for the system has flashing red LEDs and you must walk around and wave it until the cameras no longer blink. You then have to place the wand flat on the ground to set the orgin of the environment.

![IMG_8652](https://user-images.githubusercontent.com/98404383/180495459-b36c5bf2-4d38-4bd5-bdef-b6bb3eecb491.jpeg) 



### Object Identification 
Object identification is an esstencial to provide an interaction between the Vicon system, Jackal UGV, and UAV. The Jackal and UAV both had reflective markers on top of them in order for the Vicon system to recognize and locate them in the environment. Within the Vicon tracker software, you're able to highlight over them and create new objects with their names assigned. This allows for the location data to be communicated when you launch scripts.  

### Interaction 
For interaction between the hardware, Wi-Fi is used for Vicon to launch through the onboard computer within the Jackal UGV. This interaction allows the data from the Jackal UGV to be obtained and recorded. For behavioral control of the UGV, Python, and ROS are used for programming implementations. I wrote many scripts for directional movements and routes, such as a linear and square. Additionally, I created a personalized map of the lab environment used for this project. 

Vicon, a motion capture system, was utilized in the beggining of this project to learn position and localization. The Vicon specified environment was used to obtain the location of the Jackal UGV and a UAV.  





### Object Identification and Interaction. 
Object identification is an esstencial to provide an interaction between the Vicon system, Jackal UGV, and UAV. The Jackal and UAV both had reflective markers on top of them in order for the Vicon system to recognize and locate the two. Within the Vicon tracker software, you're able to highlight over them and create new objects with their names assigned. This allows for the location data to be communicated when you launch scripts.  

### Scripts
The Jackal UGV and UAV both had ROS topics of the Vicon Motion Capture system. This was done with the usage of a ROS launch file. Once the location communication was set, I created and wrote several programs for different trajectories for the Vicon environment. Each program application provided a scenario for the UAV to land on the platform while in motion. 


## Jackal UGV
To further advance with autonomous Navigation, I began working with the Jackal UGV individually. The Vicon Motion Capture System allowed an understanding of the localization of objects, however, it was within a set environment. The Jackal UGV was now going to be used to 
### Hardware
The Jackal UGV that I use  has an onboard computer that is fully integrated with ROS. Additionlly it has the clearpath ISO installed for the the computer and robotic hardware to communicate. 




### Installing ROS and Jackal Packages on Host PC

### Simulation using Gazebo and RViz





### Network Configuration of the Jackal and Host PC

### Controlling Jackal 

### Bumblebee2 (Stereo Vision Camera)

### Hokuyo UST-10LX (2D LiDAR sensor) 
















## Vicon Motion Capture System
Vicon, which is a motion capture system, was utilized in the beginning to learn the position and location of the UGV in a specified environment within the lab. The Vicon system required camera calibration and object identification to work alongside the Jackal UGV. For interaction between the two, Wi-Fi is used for Vicon to launch through the onboard computer within the Jackal UGV. This interaction allows the data from the Jackal UGV to be obtained and recorded. For behavioral control of the UGV, Python, and ROS are used for programming implementations. I wrote many scripts for directional movements and routes, such as a linear and square. Additionally, I created a personalized map of the lab environment used for this project. 

The Jackal UGV was used as the platform landing for the UAV. 


<p align="center">

</p>
