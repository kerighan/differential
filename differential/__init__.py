from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np


class Differential(object):
    def __init__(self, *args):
        self.unknowns = []
        if len(args) > 0:
            for arg in args:
                self.add_unknown(arg)
    
    def add_unknown(self, unknown):
        self.unknowns.append(unknown)
    
    def model(self, z, t):
        dzdt = []
        for i, unknown in enumerate(self.unknowns):
            dzidt = unknown.dt
            for j, unknown in enumerate(self.unknowns):
                z_j = 'z[' + str(j) + ']'
                dzidt = dzidt.replace(unknown.name, z_j)

            dzdt.append(eval(dzidt))
        return dzdt
    
    def solve(self, t):
        initials = [unknown.initial for unknown in self.unknowns]
        self.z = odeint(self.model, initials, t)
    
    def plot(self, t):
        # plot results
        for i, unknown in enumerate(self.unknowns):
            plt.plot(t, self.z[:, i], label=unknown.label)
            plt.xlabel('time')
            plt.ylabel(unknown.name)
        plt.legend(loc='best')
        plt.show()


class Repr(object):
    def __init__(self, name):
        self.name = name

    def __rmul__(self, var):
        representation = str(var) + '*' + self.name
        return Repr(representation)

    def __lmul__(self, var):
        representation = self.name + '*' + str(var)
        return Repr(representation)

    def __radd__(self, var):
        representation = str(var) + '+' + self.name
        return Repr(representation)

    def __ladd__(self, var):
        representation = self.name + '+' + str(var)
        return Repr(representation)

    def __add__(self, var):
        representation = self.name + '+' + str(var)
        return Repr(representation)

    def __sub__(self, var):
        representation = self.name + '-' + str(var)
        return Repr(representation)

    def __truediv__(self, var):
        representation = self.name + '/' + str(var)
        return Repr(representation)

    def __repr__(self):
        return self.name

    def replace(self, old_name, new_name):
        return self.name.replace(old_name, new_name)


class Unknown(Repr):
    def __init__(self, name, initial, label=None):
        self.name = name
        self.dt = 'd' + name + 'dt' 
        self.initial = initial
        self.label = label if label is not None else name
