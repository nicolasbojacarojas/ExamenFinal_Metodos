# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 

sigma = 10
beta = 2.67
rho = 28.0
dx/dt = sigma*(y-x)
dy/dt = rho * x - y - x * z
dz/dt = -beta * z + x * y
x0=0
y0=0
t0=0
