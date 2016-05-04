#-*- coding: utf-8 -*-
# MODELO APOCALIPSIS ZOMBIE (CUARANTENA)
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

P = 0           # taza de nacimiento
d = 0.0001  # porcentaje de muerte natural (por día)
B = 0.0095  # porcentaje de transmisión  (por día)
G = 0.0001  # porentaje de resurrección (por día)
A = 0.0001  # porcentaje de destrucción  (por día)
rho=1       # porcentaje de transformación
k=0.001     # porcentaje de infectados a cuarentena
sigma=0.009 # porcentaje de zombies a cuarentena
Ga=0.004    # porcentaje de muertos en cuarentena


# Resolver el sistema dy/dt = f(y, t)
def f(y, t):
    Si = y[0]
    Ii = y[1]
    Zi = y[2]
    Ri = y[3]
    Qi = y[4]
 # Ecuaciones del modelo
    f0 = P - B*Si*Zi - d*Si
    f1 = (B*Si*Zi)-(rho*Ii)-(d*Ii)-(k*Ii)
    f2 = (rho*Ii) + (G*Ri)-(A*Si*Zi)-(sigma*Zi)
    f3 = (d*Si) + (d*Ii) + (A*Si*Zi)-(G*Ri)+(Ga*Qi)
    f4 = (k*Ii)+(sigma*Zi)-(Ga*Qi)
    
    return [f0, f1, f2, f3, f4]

# condiciones iniciales
S0 = 500.                   # población inicial
Z0 = 0.                      # población zombie inicial
R0 = 0.                      # población muerta inicial
I0 = 100.                    # población infectada inicial
Q0 = 130.                    # población en cuarentena inical
y0 = [S0, Z0, R0, I0, Q0]   # vector condiciones iniclaes
t  = np.linspace(0, 10., 1000)       # tiempo

# resolviendo las ecuaciones diferenciales ordinarias
soln = odeint(f, y0, t)
S = soln[:, 0]
I = soln[:, 1]
Z = soln[:, 2]
R = soln[:, 3]
Q = soln[:, 4]

# gráfica del apocalipsis zombie (cuarentena)
plt.figure()
plt.plot(t, S, "darkcyan",linewidth=2, label='Suceptibles')
plt.plot(t, Z, "darkmagenta",linewidth=2, label='Zombies')
plt.xlabel('Dias a partir del brote de epidemia')
plt.ylabel('Poblacion')
plt.title('Apocalipsis Zombie: brote con cuarentena')
plt.legend(loc=0)
