# Obstacle-avoiding-using-TurtleBot
The following is my solution towards building an obstacle avoiding robot using TurtleBot and an onboard Lidar Sensor.

Copy the .world file and .launch file in their respective sub-folders in the turtlebot main folder.

After that create another directory and save the two python codes to it.
Then use roslaunch to run the world file (Command for my destination "roslaunch turtlebot3_gazebo turtlebot3_stage_custom.launch")
Next run the python file named "avoidance.py" (Command for me "rosrun obstacle_avoid avoidance.py")
The gazebo simulation should show motion at this point.

Finally you may run the "reading laser.py" file to get the laser readings for further use or debugging

Here is the working video for the same: https://drive.google.com/file/d/1WjnBM9lhX-xzmaFUYzKW0mhDh5vLoxCm/view?usp=sharing
