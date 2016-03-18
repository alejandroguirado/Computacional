import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
 
fig = plt.figure()
g = 9.8
x=[]
Ts=[]
i = 0
while (i<=90):
        i=i+1 
        theta0 = (i*np.pi)/180 
        l = 1 
        f = lambda x: 1/np.sqrt(np.cos(x) - np.cos(theta0)) 
        F, erri = integrate.quad(f,0,theta0)
        T = 4 * np.sqrt(l/g) * (1/np.sqrt(2)) * F
        
        x.append(i)
      
        Ts.append(T)
            
Ths = 2*np.pi*np.sqrt(l/g)
T = T/Ths

plt.xlabel('Theta_o (grados)') 
plt.ylabel('Periodo (s)')
plt.plot(x,Ts) 
plt.show()
