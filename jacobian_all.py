# This code assumes axis of revolution is the same for all joints

import sympy

# Read the input string for number of links types
info = input("Enter number of links (e.g. 4): ")
num_links = int(info)

# Define the symbols for the joint angles and velocities
thetas = sympy.symbols("theta1:{}".format(num_links+1))
dthetas = sympy.symbols("dtheta1:{}".format(num_links+1))

# Define the symbols for the link lengths
ls = sympy.symbols("l1:{}".format(num_links+1))

# Read the input string for joint types
info = input("Enter P or R for each joint (e.g. PRPP): ")
joint_types = []
for i in range(num_links):
    joint_types.append(info[i])

# Define the transformation matrices for the links
T = []
for theta, l, jt in zip(thetas, ls, joint_types):
    if jt == "P":
        T.append(sympy.Matrix([[1, 0, 0, l],
                             [0, 1, 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]]))
    elif jt == "R":
        T.append(sympy.Matrix([[sympy.cos(theta), -sympy.sin(theta), 0, l*sympy.cos(theta)],
                             [sympy.sin(theta), sympy.cos(theta), 0, l*sympy.sin(theta)],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]]))

# Compute the transformation matrix from the base frame to the end-effector frame
T_0_n = T[0]
for i in range(1, num_links):
    T_0_n = T_0_n * T[i]

# Define the end-effector position and orientation
p_ee = T_0_n[:3,3]
R_ee = T_0_n[:3,:3]


# Define the Jacobian matrix
J = sympy.zeros(6, num_links)
print(J[:3,:num_links].shape)

for i, jt in enumerate(joint_types):
    print(jt)
    if jt == "R":
        J[:3, i] = R_ee * sympy.Matrix([0, -ls[i], 0])
        J[3:, i] = R_ee * sympy.Matrix([0, 0, 1])
    elif jt == "P":
        J[:3, i] = R_ee * sympy.Matrix([0, 0, 1])
        J[3:, i] = R_ee * sympy.Matrix([0, 0, 0])

# Print the Jacobian matrix
print("Jacobian matrix:")
print(sympy.shape(J))
print(J)
#print(sympy.simplify(J))
# Substitute the values for the joint angles and velocities
subs = {theta: sympy.pi/4 for theta in thetas}
subs.update({dtheta: 0.5 for dtheta in dthetas})
J_subs = J.subs(subs)

# Print the evaluated Jacobian matrix
print("Evaluated Jacobian matrix:")
print(J_subs)
