import numpy as np
import control
import matplotlib.pyplot as plt
# Low-pass Transfer Function
wl = 0.1 #rad/s
Tfl = 1/wl
num = np.array([1])
den = np.array([Tfl , 1])
HL = control.tf(num, den)
# High-pass Transfer Function
wh = 100 #rad/s
Tfh = 1/wh
num = np.array([Tfh, 0])
den = np.array([Tfh, 1])
HH = control.tf(num, den)
# Band-pass Transfer Function
HBP = control.series(HL, HH)
print ('H(s) =', HBP)
# Frequencies
w_start = 0.01
w_stop = 1000
step = 0.01
N = int ((w_stop-w_start )/step) + 1
w = np.linspace (w_start , w_stop , N)
# Frequency Response Plot
control.bode_plot(HBP)
plt.show()