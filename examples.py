from nummath import GradientDescent
import numpy as np


def f(x):
    return x[0]**2 + x[1]**2


if __name__ == '__main__':
    x_0 = np.array([1,2])
    result = GradientDescent(max_iterations=20000).optimize(f, x_0)
    result.print()