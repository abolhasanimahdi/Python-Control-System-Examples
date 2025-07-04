import numpy as np
import matplotlib.pyplot as plt
import control
# Parameters defining the system
c = 4 # Damping constant
k = 2 # Stiffness of the spring
m = 20 # Mass
F = 5 # Force
# Simulation Parameters
tstart = 0
tstop = 60
increment = 0.1
t = np.arange(tstart,tstop+1,increment)
# System matrices
A = [[0, 1], [-k/m, -c/m]]
B = [[0], [1/m]]
C = [[1, 0]]
D = 0
sys = control.ss(A, B, C, D)
# Step response for the system
t, y, x = control.forced_response(sys, t, F, return_x=True)
plt.plot(t, y)
plt.title("Simulation of Mass-Spring-Damper System")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()

plt.figure(2)
x1 = x[0 ,:]
x2 = x[1 ,:]
plt.title("States")
plt.xlabel("t")
plt.ylabel("x1, x2")
plt.grid()
plt.plot(t, x1, t, x2)
plt.show()