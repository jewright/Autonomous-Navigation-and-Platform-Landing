# CMake generated Testfile for 
# Source directory: /home/administrator/jackal2_ws/src/jackal_robot/jackal_base
# Build directory: /home/administrator/jackal2_ws/build/jackal_robot/jackal_base
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_jackal_base_roslaunch-check_launch_base.launch "/home/administrator/jackal2_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/administrator/jackal2_ws/build/test_results/jackal_base/roslaunch-check_launch_base.launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/administrator/jackal2_ws/build/test_results/jackal_base" "/opt/ros/melodic/share/roslaunch/cmake/../scripts/roslaunch-check -o \"/home/administrator/jackal2_ws/build/test_results/jackal_base/roslaunch-check_launch_base.launch.xml\" \"/home/administrator/jackal2_ws/src/jackal_robot/jackal_base/launch/base.launch\" ")
add_test(_ctest_jackal_base_roslint_package "/home/administrator/jackal2_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/administrator/jackal2_ws/build/test_results/jackal_base/roslint-jackal_base.xml" "--working-dir" "/home/administrator/jackal2_ws/build/jackal_robot/jackal_base" "--return-code" "/opt/ros/melodic/share/roslint/cmake/../../../lib/roslint/test_wrapper /home/administrator/jackal2_ws/build/test_results/jackal_base/roslint-jackal_base.xml make roslint_jackal_base")
