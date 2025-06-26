import numpy as np
import matplotlib.pyplot as plt
import control
K = 3
T = 4
num = np.array ([K])
den = np.array ([T , 1])
H1 = control.tf(num , den)
print ('H1(s) =', H1)
Tau = 2
N = 20 # Order of the Approximation
[num_pade,den_pade] = control.pade(Tau,N)
Hpade = control.tf(num_pade,den_pade)
print ('Hpade(s) =', Hpade)
H = control.series(H1, Hpade)
print ('H(s) =', H)
t, y = control.step_response(H)
plt.plot(t,y)
plt.title("H(s)")
plt.grid()
plt.show()