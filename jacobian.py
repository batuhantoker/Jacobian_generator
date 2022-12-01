import sympy

# Define the number of links in the robot
num_links = 4

# Define the symbols for the joint angles and velocities
thetas = sympy.symbols("theta1:{}".format(num_links+1))
dthetas = sympy.symbols("dtheta1:{}".format(num_links+1))

# Define the symbols for the link lengths
ls = sympy.symbols("l1:{}".format(num_links+1))

# Define the transformation matrices for the links
T = [sympy.Matrix([[sympy.cos(theta), -sympy.sin(theta), 0, l],
                   [sympy.sin(theta), sympy.cos(theta), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
     for theta, l in zip(thetas, ls)]

# Compute the transformation matrix from the base frame to the end-effector frame
T_0_n = T[0]
for i in range(1, num_links):
    T_0_n = T_0_n * T[i]

# Define the end-effector position and orientation
p_ee = T_0_n[:3,3]
R_ee = T_0_n[:3,:3]

# Define the Jacobian matrix
J = sympy.zeros(6, num_links)
J[:3,:num_links] = R_ee * sympy.Matrix([[0, -l, 0] for l in ls[1:]])
J[3:,:num_links] = R_ee * sympy.Matrix([[-sympy.sin(theta), -l*sympy.cos(theta), 0] for theta, l in zip(thetas[1:], ls[1:])])

# Print the Jacobian matrix
print("Jacobian matrix:")
print(J)

# Substitute the values for the joint angles and velocities
subs = {theta: sympy.pi/4 for theta in thetas}
subs.update({dtheta: 0.5 for dtheta in dthetas})
J_subs = J.subs(subs)

# Print the evaluated Jacobian matrix
print("Evaluated Jacobian matrix:")
print(J_subs)
