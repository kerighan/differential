from differential import Differential, Unknown
import numpy as np

# initial condition
alpha = 2 / 3
beta = 4 / 3
gamma = 1
delta = 1

# create unknowns
x = Unknown('x', 2, label='proie')  # proie
y = Unknown('y', 1.5, label='prédateur')  # prédateur

# write down equation
x.dt = alpha * x - beta * x * y
y.dt = delta * x * y - gamma * y

# time points
t = np.linspace(0, 20, 1000)

# solve ODE
diff = Differential(x, y)
diff.solve(t)
diff.plot(t)
