#-*- coding: utf-8 -*-
# MODELO APOCALIPSIS ZOMBIE (INFECCIÓN LATENTE)
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

P = 0           # taza de nacimiento
d = 0.0001  # porcentaje de muerte (por día)
B = 0.0095  # porcentaje de transmisión  (por día)
G = 0.0001  # porcentaje de resurrección (por día)
A = 0.0001  # porcentaje de destrucción  (por día)
rho = 0.3   # porcentaje de transformación (por día)

# Resolver el sistema dy/dt = f(y, t)
def f(y, t):
    Si = y[0]
    Ii = y[1]
    Zi = y[2]
    Ri = y[3]
  
 # Ecuaciones del modelo
    f0 = P - B*Si*Zi - d*Si
    f1 = B*Si*Zi - rho*Ii - d*Ii
    f2 = rho*Ii + G*Ri - A*Si*Zi
    f3 = d*Si + d*Ii + A*Si*Zi - G*Ri
    return [f0, f1, f2, f3]

# condiciones iniciales
S0 = 500.                   # población inicial
I0 = 1.                     # población infectada inicial
Z0 = 0.                     # población zombie inicial
R0 = 0.                     # población muerta inicial

y0 = [S0, I0, Z0, R0]   # vector condiciones iniciales
t  = np.linspace(0, 20, 1000)       # tiempo

# resolviendo las ecuaciones diferenciales ordinarias
soln = odeint(f, y0, t)
S = soln[:, 0]
I = soln[:, 1]
Z = soln[:, 2]
R = soln[:, 3]


# gráfica de apocalipsis zombie con infección latente
plt.plot(t, S, "darkcyan",linewidth=2, label='Suceptibles')
plt.plot(t, Z, "darkmagenta",linewidth=2, label='Zombies')
plt.xlabel('Dias a partir del brote de epidemia')
plt.ylabel('Poblacion')
plt.title('Apocalipsis Zombie: infeccion latente')
plt.legend(loc=0)
