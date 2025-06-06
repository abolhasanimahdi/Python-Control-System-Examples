import numpy as np  # Import numpy for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting

def first_order_response(K, T, start_time, stop_time, increment):
    t = np.arange(start_time, stop_time, increment)  # Time vector
    y = K * (1 - np.exp(-t / T))  # System response
    return t, y

start_time = 0
stop_time = 30

K = 3
T = 4
t1, y1 = first_order_response(K, T, start_time, stop_time, 0.1)
K = 4
T = 5
t2, y2 = first_order_response(K, T, start_time, stop_time, 0.1)

# Plot both responses on the same figure
plt.figure(figsize=(8, 5))
plt.plot(t1, y1, label='K = 3, T = 4')
plt.plot(t2, y2, label='K = 4, T = 5', linestyle='--')
plt.title('First Order System Step Response')
plt.xlabel('Time (seconds)')
plt.ylabel('Output y(t)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
