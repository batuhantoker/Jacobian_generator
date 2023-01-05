# Jacobian_generator
 a Python script that can generate the Jacobian matrix of any robot
 
This script defines the number of links in the robot from user input, and then creates the transformation matrices for each link using rotation and translation matrices. 

It first computes the transformation matrix from the base frame to the end-effector frame, and defines the end-effector position and orientation using this matrix. 

The Jacobian matrix is then computed using the end-effector position, orientation, and link lengths, and is printed to the console. 

You can modify the code to suit your specific needs and to compute the Jacobian matrix for different values of the joint angles and velocities.
