import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Control import ControlClass

# Simulation Parameters
yk = 0
uk = 1
Tstop = 30
Ts = 0.5
N = int(Tstop / Ts)  # Simulation length

# Controller Initialization
r = 1
Kp = 1
Ti = 5
u_prev = 0
e_prev = 0
control = ControlClass(Ts, Kp, Ti)

# Data containers
data = [yk]
time = [0]

# Plot setup
fig, ax = plt.subplots()
line, = ax.plot([], [], '-*', label='Output y(t)')
ax.set_xlim(0, Tstop)
ax.set_ylim(0, 1.5)  # Adjust as needed based on expected system response
ax.set_title('Control of 1st Order Dynamic System')
ax.set_xlabel('t [s]')
ax.set_ylabel('y(t)')
ax.grid()
ax.legend()

# Animation update function
k = [0]  # Using a list to make it mutable inside the function
def update(frame):
    global yk, u_prev, e_prev
    u, e = control.Controller(yk, r, u_prev, e_prev)
    u_prev = u
    e_prev = e
    yk1 = control.Model(yk, u)
    yk = yk1
    data.append(yk1)
    time.append((k[0] + 1) * Ts)
    line.set_data(time, data)
    k[0] += 1
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=N, interval=Ts * 1000, repeat=False)

plt.show()
