from differential import Repr


def sin(r):
    representation = 'np.sin(' + r.name + ')'
    return Repr(representation)


def cos(r):
    representation = 'np.cos(' + r.name + ')'
    return Repr(representation)


def tan(r):
    representation = 'np.tan(' + r.name + ')'
    return Repr(representation)


def exp(r):
    representation = 'np.exp(' + r.name + ')'
    return Repr(representation)


def square(r):
    representation = 'np.square(' + r.name + ')'
    return Repr(representation)


def sqrt(r):
    representation = 'np.sqrt(' + r.name + ')'
    return Repr(representation)
