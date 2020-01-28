import numpy as np


class Optimizer():

    def __init__(self):
        self.epsilon_mach = 1.1102230246251565e-16
        self.step_length_derivatives = 1.0536712127723509e-08

    def derive(self, f, x):
        h = self.step_length_derivatives
        dimension_domain = len(x)
        result = np.empty(dimension_domain)

        for i in range(dimension_domain):
            e = self._get_unit_vector(dimension_domain,i)
            result[i] = (f(x + h * e) - f(x - h * e)) / (2 * h)

        return result

    def _get_unit_vector(self, dimension, index):
        unit_vector = np.zeros([dimension])
        unit_vector[index] = 1
        return unit_vector


if __name__ == '__main__':
    opt = Optimizer()
    d = opt.derive(lambda x: x ** 2, np.array([5]))
    print(d)
