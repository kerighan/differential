from differential import Differential, Unknown
from tqdm import tqdm
import numpy as np


N = 100  # number of people
num_recovered = 0  # initial number of recovered people
num_infectious = 1  # initial number of infected people
num_susceptible = N - num_infectious - num_recovered

# define unknowns
S = Unknown('S', num_susceptible, 'susceptible')
I = Unknown('I', num_infectious, 'infectious')
R = Unknown('R', num_recovered, 'recovered')

# parameters
beta = .001  # disease ratio
gamma = .0001  # recovery ratio
mu = .0  # population birth rate
nu = .0  # population death rate
xi = 0.0  # ratio of recovered people who become susceptible again

# SIRS equations with vital dynamics
S.dt = -beta * S * I / N + mu * N -nu * S + xi * R
I.dt = beta * S * I / N - gamma * I - nu * I
R.dt = gamma * I - nu * R - xi * R

# time points
t = np.linspace(0, 3500, 300)

# solve ODE
diff = Differential(S, I, R)
diff.solve(t)
diff.plot(t)
