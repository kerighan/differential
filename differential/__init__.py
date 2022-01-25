import matplotlib.pyplot as plt
import numpy as np
from pytest import param
from scipy.integrate import odeint


def name_or_value(func):
    def wrapper(self, var):
        if isinstance(var, Repr):
            var = var.name

        res = func(self, var)
        return res
    return wrapper


class Repr(object):
    def __init__(self, name):
        self.name = name

    @name_or_value
    def __mul__(self, var):
        representation = f"({self.name}*{var})"
        return Repr(representation)

    @name_or_value
    def __rmul__(self, var):
        representation = f"({var}*{self.name})"
        return Repr(representation)

    @name_or_value
    def __lmul__(self, var):
        representation = f"({self.name}*{var})"
        return Repr(representation)

    @name_or_value
    def __radd__(self, var):
        representation = f"({var}+{self.name})"
        return Repr(representation)

    @name_or_value
    def __ladd__(self, var):
        representation = f"({self.name}+{var})"
        return Repr(representation)

    @name_or_value
    def __add__(self, var):
        representation = f"({self.name}+{var})"
        return Repr(representation)

    @name_or_value
    def __sub__(self, var):
        representation = f"({self.name}-{var})"
        return Repr(representation)

    @name_or_value
    def __lsub__(self, var):
        print(var)
        representation = f"({self.name}-{var})"
        return Repr(representation)

    @name_or_value
    def __rsub__(self, var):
        representation = f"({var}-{self.name})"
        return Repr(representation)

    @name_or_value
    def __truediv__(self, var):
        representation = f"({self.name}/{var})"
        return Repr(representation)

    def __neg__(self):
        representation = f"(-{self.name})"
        return Repr(representation)

    def __repr__(self):
        return self.name

    # def __str__(self):
    #     return self.name.replace("<", "").replace(">", "")

    def replace(self, old_name, new_name):
        return self.name.replace(old_name, new_name)


class Unknown(Repr):
    def __init__(self, name, initial, label=None):
        self.name = f"_{name}_"
        self.dt = f"d{self.name}dt"
        if isinstance(initial, Parameter):
            self._initial_is_param = True
        else:
            self._initial_is_param = False
        self.initial = initial
        self.label = label if label is not None else name

    def get_initial(self):
        if not self._initial_is_param:
            return self.initial
        else:
            return self.initial.value


class Parameter(Repr):
    def __init__(self, name, value=None):
        self.name = f"_{name}_"
        self.value = value


class Differential(object):
    def __init__(self, *args):
        self.unknowns = []
        self.parameters = {}
        if len(args) > 0:
            for arg in args:
                self.add(arg)

    def add(self, item):
        if isinstance(item, Unknown):
            self.unknowns.append(item)
        else:
            self.parameters[item.name] = item

    def model(self, z, t):
        dzdt = []
        for unknown in self.unknowns:
            dzidt = unknown.dt
            for j, unknown in enumerate(self.unknowns):
                dzidt = dzidt.replace(unknown.name, f"z[{j}]")
            for parameter in self.parameters.values():
                dzidt = dzidt.replace(parameter.name, str(parameter.value))
            dzdt.append(eval(dzidt))
        return dzdt

    def evaluate_unknown(self, unknown):
        initial = unknown.get_initial()
        if isinstance(initial, Repr):
            initial = str(initial)
            for param in self.parameters.values():
                initial = initial.replace(param.name, str(param.value))
            initial = eval(initial)
        return initial

    def solve(self, t, **kwargs):
        for key, val in kwargs.items():
            self.parameters[f"_{key}_"].value = val

        initials = [self.evaluate_unknown(unknown)
                    for unknown in self.unknowns]
        return odeint(self.model, initials, t)

    def plot(self, t, z):
        # plot results
        for i, unknown in enumerate(self.unknowns):
            plt.plot(t, z[:, i], label=unknown.label)
            plt.xlabel('time')
            plt.ylabel(unknown.name.replace("_", ""))
        plt.legend(loc='best')
        plt.show()
