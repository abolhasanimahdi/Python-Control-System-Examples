import numpy as np  # Import numpy for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import scipy.integrate as scipy

start_time = 0
stop_time = 40
K = 3
T = 4
u = 1
y0 = 0
Increment = 0.1

t = np.arange(start_time, stop_time, Increment)  # Time vector
y1 = K * (1 - np.exp(-t / T))  # System response

def system(y, t, K, T, u):
    dydt = (K * u - y) / T
    return dydt

y2 = scipy.odeint(system, y0, t, args = (K, T, u))

# Plot both responses on the same figure
plt.figure(figsize=(8, 5))
plt.plot(t, y1, label='Simulate Time Domain Response')
plt.plot(t, y2, label='Solve ODE', linestyle='--')
plt.title(r"$\dot{y} = \frac{1}{%d}(%du - y)$" % (T, K))
plt.xlabel('Time (seconds)')
plt.ylabel('Output y(t)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()