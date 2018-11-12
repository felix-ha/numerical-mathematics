from optimization.gradient_descent import GradientDescent
import numpy as np
from functions import f_1


if __name__ == '__main__':
    x_0 = np.array([1,2])
    result = GradientDescent(max_iterations=20000).optimize(f_1, x_0)
    result.print()