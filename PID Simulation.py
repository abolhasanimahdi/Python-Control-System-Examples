import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Control import ControlClass

# Initial state
yk = 0
uk = 1
Ts = 0.5

# Controller initialization
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
ax.set_xlim(0, 0)  # Initial range, will auto-expand
ax.set_ylim(0, 1.5)
ax.set_title('Control of 1st Order Dynamic System')
ax.set_xlabel('t [s]')
ax.set_ylabel('y(t)')
ax.grid()
ax.legend()

# Animation update function
k = [0]
def update(frame):
    global yk, u_prev, e_prev
    u, e = control.Controller(yk, r, u_prev, e_prev)
    u_prev = u
    e_prev = e
    yk1 = control.Model(yk, u)
    yk = yk1
    k[0] += 1
    data.append(yk1)
    time.append(k[0] * Ts)

    # Dynamically update axes
    if time[-1] > ax.get_xlim()[1]:
        ax.set_xlim(0, time[-1] + 6)
        ax.figure.canvas.draw()

    line.set_data(time, data)
    return line,

# Create infinite animation
ani = FuncAnimation(fig, update, interval=Ts * 1000, blit=True, cache_frame_data=False)

plt.show()
