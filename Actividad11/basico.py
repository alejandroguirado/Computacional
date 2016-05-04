#-*- coding: utf-8 -*-

# APOCALIPSIS ZOMBIE (MODELO BÁSICO)
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

P = 0           # taza de nacimientos
d = 0.0001      # porcentaje de muerte natural (por día)
B = 0.0095      # porcentaje de transmisión (por día)
G = 0.0001      # porcentaje de resurrección (por día)
A = 0.0001      # porcentaje de destrucción (por día)

# Resolver el sistema dy/dt = f(y, t)
def f(y, t):
    Si = y[0]
    Zi = y[1]
    Ri = y[2]
 # Ecuaciones del modelo    
    f0 = P - B*Si*Zi - d*Si
    f1 = B*Si*Zi + G*Ri - A*Si*Zi
    f2 = d*Si + A*Si*Zi - G*Ri
    return [f0, f1, f2]
# condiciones iniciales 
S0 = 500.                       # población inicial
Z0 = 0                          # población zombie inicial
R0 = 100                        # población muerta inicial
y0 = [S0, Z0, R0]               # vector condiciones iniclaes
t  = np.linspace(0, 5., 1000)   # tiempo

# resolviendo las ecuaciones diferenciales ordinarias
soln = odeint(f, y0, t)
S = soln[:, 0]
Z = soln[:, 1]
R = soln[:, 2]

# gráfica del modelo básico de apocalipsis zombie
plt.figure()
plt.plot(t, S, "darkcyan",linewidth=2, label='Suceptibles')
plt.plot(t, Z, "darkmagenta",linewidth=2, label='Zombies')
plt.xlabel('Dias a partir del brote de epidemia')
plt.ylabel('Poblacion')
plt.title('Apocalipsis Zombie: modelo basico')
plt.legend(loc=0)
