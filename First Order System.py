import numpy as np
import matplotlib.pyplot as plt

K = 3
T = 4

StartTime = 0
StopTime = 30

Increment = 0.1
t = np.arange(StartTime, StopTime, Increment)

y = K * (1 - np.exp(-t/T))

plt.plot(t, y)
plt.title('Title')
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.show()
