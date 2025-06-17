import numpy as np
import control
import matplotlib.pyplot as plt

# Define Transfer Function
num1 = np.array([3])
num2 = np.array([2, 1])
num = np.convolve(num1, num2)
den1 = np.array([3, 1])
den2 = np.array([5, 1])
den = np.convolve(den1, den2)

H = control.tf(num, den)
print ('H(s) =', H)

# Bode Plot
control.bode(H)
plt.show()