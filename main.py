# Project 6 Numeric Computations with Taylor Polynomials CST-305
# Rodrigo Gomez
# Description: Taylor Polynomial methods for solving differential equations
# Packages numpy and matplotlib

import numpy as np
import matplotlib.pyplot as plt

# PART 1 (a)
def taylor_part1a(x):
    return 1 - x - (x**3)/3 - (x**4)/12

x_vals = np.linspace(0, 4, 100)
y_vals = taylor_part1a(x_vals)

plt.figure()
plt.plot(x_vals, y_vals)
plt.title("Part 1(a): Taylor Approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
print("Value at x = 3.5:", round(taylor_part1a(3.5), 2))


# PART 1 (b)
def taylor_part1b(x):
    return 6 + (x - 3) - (11/2)*(x - 3)**2

x_vals = np.linspace(2, 4, 100)
y_vals = taylor_part1b(x_vals)

plt.figure()
plt.plot(x_vals, y_vals)
plt.title("Part 1(b): Taylor Polynomial")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()


# PART 2
def numerical_part2(x):
    return x / (x**2 + 4)
x_vals = np.linspace(-2, 2, 100)
y_vals = numerical_part2(x_vals)
plt.figure()
plt.plot(x_vals, y_vals)
plt.title("Part 2: Numerical Approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()


# PART 3
def performance(t, P):
    return 42.75 - 0.576 * P

t_vals = np.linspace(0, 10, 100)
P_vals = []
P = 0  # initial condition

for t in t_vals:
    P = P + 0.1 * performance(t, P)  # Euler method
    P_vals.append(P)

plt.figure()
plt.plot(t_vals, P_vals)
plt.title("Part 3: System Performance Model")
plt.xlabel("Time")
plt.ylabel("Performance")
plt.grid()
plt.show()