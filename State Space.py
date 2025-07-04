import numpy as np
import control
import matplotlib.pyplot as plt
# Define State-space Model
A = [[0, 1], [-1, -3]]
B = [[1], [0]]
C = [[5, 6]]
D = [[1]]

start = 0
stop = 200
step = 0.1
t = np.arange(start, stop + 1, step)

ssmodel = control.ss(A, B, C, D)
u = 1

# Step response for the system
t, y, x = control.forced_response(ssmodel, t, u, return_x=True)

plt.figure(1)
plt.plot(t, y)
plt.title("Step Response")
plt.xlabel("t")
plt.ylabel("y")
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