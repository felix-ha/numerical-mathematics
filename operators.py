'''
Implementations of differential operators
'''

import numpy as np


def f(x):
    return np.array([x[1] ** 2, x[0]**2, x[0] + x[2]])


def derive(f, x):
    h = 0.01
    dimension_domain = len(x)
    dimension_value = len(f(x))

    if dimension_value == 1:
        result = np.empty(dimension_domain)

        for i in range(dimension_domain):
            e = _get_unit_vector(dimension_domain, i)
            result[i] = (f(x + h * e) - f(x - h * e)) / (2 * h)

        return result
    else:
        result = np.empty([dimension_value, dimension_domain])
        for j in range(dimension_value):
            gradient = np.empty(dimension_domain)
            for i in range(dimension_domain):
                e = _get_unit_vector(dimension_domain, i)
                gradient[i] = (f(x + h * e)[j] - f(x - h * e)[j]) / (2 * h)
            result[j, :] = gradient

        return result


def _get_unit_vector(dimension, index):
    unit_vector = np.zeros([dimension])
    unit_vector[index] = 1
    return unit_vector


if __name__ == '__main__':
    x_0 = np.array([1, 1, 7])
    print(f(x_0))
    print(derive(f, x_0))
