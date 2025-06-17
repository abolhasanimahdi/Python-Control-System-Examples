import control
import numpy as np  # Numerical operations
import matplotlib.pyplot as plt  # Plotting
import scipy.integrate as integrate  # ODE solver
import scipy.signal as sig  # ODE solver

# System parameters
K = 3       # Gain
T = 4       # Time constant
u = 1       # Input
y0 = 0      # Initial output
a = -1/T
b = K/T
# Simulation time parameters
start_time = 0
stop_time = 40
increment = 0.1

Ts = 1
uk = 1
yk = 0
N = int(stop_time/Ts)
data = []
data.append(yk)

num = np.array([K])
den = np.array([T, 1])
# Time vector
t = np.arange(start_time, stop_time, increment)
td = np.arange(start_time, stop_time+Ts, Ts)
# Analytical solution of first order system step response
y_analytical = K * (1 - np.exp(-t / T))

# Define system differential equation
def system(y, t, K, T, u):
    dydt = (K * u - y) / T
    return dydt

# Numerical solution using ODE solver
y_numerical = integrate.odeint(system, y0, t, args=(K, T, u))

for k in range(N):
    yk1 = (1 + a * Ts) * yk + Ts * b * uk
    yk = yk1
    data.append(yk1)

H = control.tf(num, den)
print('H(s) =', H)

tt, y_Transfer = control.step_response(H)

# Plot both responses
plt.figure(figsize=(8, 5))
plt.plot(t, y_analytical, label='Analytical Solution')
plt.plot(t, y_numerical, label='Numerical Solution (ODE)', linestyle='--')
plt.plot(td, data, label='Discrete', linestyle='--')
plt.plot(tt, y_Transfer, label='Transfer Function', linestyle='--')
plt.title(r"$\dot{y} = \frac{1}{%d}(%du - y)$" % (T, K))
plt.xlabel('Time (seconds)')
plt.ylabel('Output y(t)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()