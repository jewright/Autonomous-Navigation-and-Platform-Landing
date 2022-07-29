#!/usr/bin/env python
__author__ = 'Mushahid Rasul'
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import axes3d
from numpy import sin, cos, pi, outer, ones, size, linspace
# ##################################################################################################################
# Linear Trajectory
# ##################################################################################################################
# data = pd.read_csv("/home/mushahid/ros-intel-uav-rpeo/simulation_ws/src/pie/script/Scenarios/Linear_Traj/Linear_Traj_Data_1.csv")

# # Velocity vs. Time Graph
# fig0 = plt.figure(0)
# plt.plot(data['time'],data['Jackal_x_vel'],'b',label= "Jackal_linear_velocity_x")
# plt.plot(data['time'],data['Jackal_y_vel'],'g',label= "Jackal_linear_velocity_y")
# plt.plot(data['time'],data['Jackal_z_vel'],'r',label= "Jackal_linear_velocity_z")
# plt.plot(data['time'],data['UAV_x_vel'],'b',label= "UAV_linear_velocity_x")
# plt.plot(data['time'],data['UAV_y_vel'],'g',label= "UAV_linear_velocity_y")
# plt.plot(data['time'],data['UAV_z_vel'],'r',label= "UAV_linear_velocity_z")

# plt.title("Jackal/UAV Velocity VS. Time Graph for LINEAR TRAJECTORY \n Rough Terrain")
# plt.xlabel("Time (s)")
# plt.ylabel("Linear Velocity (m/s)")
# plt.legend(loc='best')
# plt.legend(["Jackal_linear_velocity_x", "Jackal_linear_velocity_y", "Jackal_linear_velocity_z",
#             "UAV_x_vel", "UAV_y_vel", "UAV_z_vel"])
# # Position vs. Time Graph
# fig1 = plt.figure(1)
# plt.plot(data['time'],data['Jackal_x_pos'],'c',label= "Jackal_position_x")
# plt.plot(data['time'],data['Jackal_y_pos'],'m',label= "Jackal_position_y")
# plt.plot(data['time'],data['Jackal_z_pos'],'y',label= "Jackal_position_z")
# plt.plot(data['time'],data['UAV_x_pos'],'c',label= "UAV_position_x")
# plt.plot(data['time'],data['UAV_y_pos'],'m',label= "UAV_position_y")
# plt.plot(data['time'],data['UAV_z_pos'],'y',label= "UAV_position_z")

# plt.title("Jackal/UAV Position VS. Time Graph for LINEAR TRAJECTORY \n Rough Terrain")
# plt.xlabel("Time (s)")
# plt.ylabel("Position (m)")
# plt.legend(loc='best')
# plt.legend(["Jackal_position_x", "Jackal_position_y", "Jackal_position_z",
#             "UAV_x_pos", "UAV_y_pos","UAV_z_pos"])
# ##########################################################################################################
# # 3D Jackal-Position Graph
# fig1 = plt.figure(figsize=plt.figaspect(0.5))
# ax = fig1.add_subplot(1,2,1,projection='3d')
# ax.set_title('Jackals Position 3D plot for LINEAR TRAJECTORY') 
# x = data["Jackal_x_pos"]
# y = data["Jackal_y_pos"] 
# z = data['Jackal_z_pos']
# ax.plot(x, y, z, label='Jackals 3D Pose')
# ax.set_xlabel('X-Axis')
# ax.set_ylabel('Y-Axis')
# ax.set_zlabel('Z-Axis')
# ax.set_xlim(-1, 7)
# ax.set_ylim(-1, 1)
# ax.set_zlim(0, 1)
# ax.legend()
# # 3D UAV-Position Graph
# ax = fig1.add_subplot(1,2,2,projection='3d')
# ax.set_title('UAVs Position 3D plot for LINEAR TRAJECTORY')
# z = data["UAV_x_pos"] 
# x = data["UAV_y_pos"]
# y = data["UAV_z_pos"] 
# ax.plot(x, y, z, label='UAVs 3D Pose')
# ax.set_xlabel('X-Axis')
# ax.set_ylabel('Y-Axis')
# ax.set_zlabel('Z-Axis')
# ax.set_xlim(-1, 8)
# ax.set_ylim(-1, 6)
# ax.set_zlim(0, 8)
# ax.legend()
# plt.show()

# ##################################################################################################################
# # Square Trajectory
# ##################################################################################################################

# ###############
# #   Velocity  #
# ###############

# data2 = pd.read_csv("/home/mushahid/ros-intel-uav-rpeo/simulation_ws/src/pie/script/Scenarios/Square_Traj/velocity/Jackal_0_UAV_0_Square_Velocity_XYZ.csv")

# fig2 = plt.figure(2)
# plt.plot(data2['sim_time'],data2[' Jackal0:linear_velocity/x'],'b',label= "Jackal_linear_velocity_x")
# plt.plot(data2['sim_time'],data2[' Jackal0:linear_velocity/y'],'g',label= "Jackal_linear_velocity_y")
# plt.plot(data2['sim_time'],data2[' Jackal0:linear_velocity/z'],'r',label= "Jackal_linear_velocity_z")
# plt.plot(data2['sim_time'],data2[' Uav0:linear_velocity/x']   ,'c',label= "UAV_linear_velocity_x")
# plt.plot(data2['sim_time'],data2[' Uav0:linear_velocity/y']   ,'m',label= "UAV_linear_velocity_y")
# plt.plot(data2['sim_time'],data2[' Uav0:linear_velocity/z']   ,'y',label= "UAV_linear_velocity_z")

# plt.title("Jackal and UAV Velocity VS. Time Graph for SQUARE TRAJECTORY")
# plt.xlabel("Time (s)")
# plt.ylabel("Linear Velocity (m/s)")
# plt.legend(loc='best')
# plt.legend(["Jackal_linear_velocity_x", "Jackal_linear_velocity_y", "Jackal_linear_velocity_z",
#             "UAV_linear_velocity_x", "UAV_linear_velocity_y", "UAV_linear_velocity_z"])

# ###############
# #   Position  #
# ###############

# data3 = pd.read_csv("/home/mushahid/ros-intel-uav-rpeo/simulation_ws/src/pie/script/Scenarios/Square_Traj/position/terrain/Square_Traj0_JACKAL.csv")
# data4 = pd.read_csv("/home/mushahid/ros-intel-uav-rpeo/simulation_ws/src/pie/script/Scenarios/Square_Traj/position/terrain/Square_Traj0_UAV.csv")
# fig3 = plt.figure(3)
# plt.plot(data3['time'],data3['x_jackal'],'y',label= "Jackal_Position_x")
# plt.plot(data3['time'],data3['y_jackal'],'k',label= "Jackal_Position_y")
# plt.plot(data4['time'],data4['x_uav'],'r',label= "UAV_Position_x")
# plt.plot(data4['time'],data4['y_uav'],'g',label= "UAV_Position_y")
# plt.plot(data4['time'],data4['z_uav'],'b',label= "UAV_Position_z")

# plt.title("Jackal and UAV Position VS. Time Graph for SQUARE TRAJECTORY\n With Speed Bumps")
# plt.xlabel("Time (s)")
# plt.ylabel("Position (m)")
# plt.legend(loc='best')
# plt.legend(["Jackal_Position_x", "Jackal_Position_y",
#             "UAV_Position_x", "UAV_Position_y", "UAV_Position_z"])

# # plt.show()

# fig = plt.figure(figsize=plt.figaspect(0.5))
# ax = fig.add_subplot(1,2,1,projection='3d')
# ax.set_title('Jackals Position 3D plot for SQUARE TRAJECTORY')
# x = data3["x_jackal"]
# y = data3["y_jackal"] 
# ax.plot(x, y, label='Jackals 3D Pose')
# ax.set_xlabel('X-Axis')
# ax.set_ylabel('Y-Axis')
# ax.set_zlabel('Z-Axis')
# ax.set_xlim(-1, 8)
# ax.set_ylim(-1, 8)
# ax.set_zlim(0, 1)
# ax.legend()

# ax = fig.add_subplot(1,2,2,projection='3d')
# ax.set_title('UAVs Position 3D plot for SQUARE TRAJECTORY')
# z = data4["z_uav"] 
# x = data4["x_uav"]
# y = data4["y_uav"] 
# ax.plot(x, y, z, label='UAVs 3D Pose')
# ax.set_xlabel('X-Axis')
# ax.set_ylabel('Y-Axis')
# ax.set_zlabel('Z-Axis')
# ax.set_xlim(-1, 12)
# ax.set_ylim(-1, 8)
# ax.set_zlim(0, 5)
# ax.legend()
# plt.show()

# ##################################################################################################################
# # Circle Trajectory
# ##################################################################################################################
# data6 = pd.read_csv("/home/administrator/ros-intel-uav-rpeo/jackal2_ws/src/offbordctrl/script/data_log/UGV_Circular_Trajectory.csv")
data6 = pd.read_csv("/home/administrator/ros-intel-uav-rpeo/jackal2_ws/src/offbordctrl/script/data_log/trial_1.csv")

# ctime1 =  data1['time']
# xpos1  =  data1['X_POS'] 
# ypos1  =  data1['Y_POS'] 
# zpos1  =  data1['Z_POS']

# # ctime2 =  data2['time']
# # xpos2  =  data2['X_POS'] 
# # ypos2  =  data2['Y_POS'] 
# # zpos2  =  data2['Z_POS']

# fig = plt.figure()
# ax = p3.Axes3D(fig)

# def gen(n):
#     phi = 0
#     while phi < 2*np.pi:
#         yield np.array([np.cos(phi), np.sin(phi), phi])
#         phi += 2*np.pi/n

# def update(num, data, line):
#     line.set_data(data[:2, :num])
#     line.set_3d_properties(data[2, :num])

# N = 100
# data = np.array(list(gen(N))).T
# line, = ax.plot(xpos1[i], ypos1[i], zpos1[i])

# # Setting the axes properties
# ax.set_xlim3d([-1.0, 1.0])
# ax.set_xlabel('X')

# ax.set_ylim3d([-1.0, 1.0])
# ax.set_ylabel('Y')

# ax.set_zlim3d([0.0, 10.0])
# ax.set_zlabel('Z')

# ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=10000/N, blit=False)
# #ani.save('matplot003.gif', writer='imagemagick')
# plt.show()
# ###############
# #   Velocity  #
# ###############
# plt.plot(data6['time'],data6['X_Vel'],'c',label= "UGV_Vel_x")
# plt.plot(data6['time'],data6['Y_Vel'],'m',label= "UGV_Vel_y")
# plt.plot(data6['time'],data6['Z_Vel'],'y',label= "UGV_Vel_z")

# plt.title("UGV Vel VS. Time Graph for CIRCLE TRAJECTORY")
# plt.xlabel("Time (s)")
# plt.ylabel("Vel (m/s)")
# plt.legend(loc='best')
# plt.legend(["UGV_Vel_x", "UGV_Vel_y", "UGV_Vel_z"])
# plt.show()

# # ###############
# # #   Position  #
# # ###############

fig4 = plt.figure(1)

plt.plot(data6['time'],data6['X_POS'],'r',label= "UGV_Position_x")
plt.plot(data6['time'],data6['Y_POS'],'g',label= "UGV_Position_y")
plt.plot(data6['time'],data6['Z_POS'],'b',label= "UGV_Position_z")

plt.title("UGV Position VS. Time Graph for CIRCLE TRAJECTORY")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend(loc='best')
plt.legend(["UGV_Position_x", "UGV_Position_y", "UGV_Position_z"])
plt.show()

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1,1,1,projection='3d')
ax.set_title('UGVs Position 3D plot for CIRCLE TRAJECTORY')
x = data6["X_POS"]
y = data6["Y_POS"] 
z = data6["Z_POS"] 
ax.plot(x, y, z, label='UGVs 3D Pose')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.set_zlim(0, 7)
ax.legend()
plt.show()
