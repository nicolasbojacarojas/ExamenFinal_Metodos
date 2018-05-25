#Ejercicio3
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Grafique las dos series de datos en una misma imagen 'serie.png'
# Calcule la covarianza entre `u` y `v` e imprima su valor.

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t = np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6, 0.8, 0.9])
u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])
def cov(u, v):
    pu = np.mean(u)
    pv = np.mean(v)
    puntos = len(u)
    varuv = np.sum((u-pu)*(v-pv))/puntos
    return varuv
plt.plot(t, v, label = "serie de v")
plt.plot(t, u, label = 'serie de u')
plt.legend(loc = 0)
plt.savefig('serie.png')
print (cov(u,v))
    
    