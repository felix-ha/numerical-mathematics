import numpy as np
from operators import derive


def f(x):
    return x ** 2 - 9


def F(x):
    return np.array([x[0] ** 2 - 9, x[1] ** 2 - 36])


def newton(f, x_0):
    try:
        dimension_domain = len(x_0)
    except TypeError:
        dimension_domain = 1

    x_current = x_0
    f_current = f(x_current)

    while np.linalg.norm(f_current) > 0.001:
        f_current = f(x_current)
        jacobian = derive(f, x_current)
        if dimension_domain == 1:
            x_delta = - (1 / jacobian) * f_current
        else:
            x_delta = np.linalg.solve(jacobian, -f_current)

        x_next = x_current + x_delta
        x_current = x_next

    return x_current

x_0 = np.array([4, 4])
# x_0 = 4
x_star = newton(F, x_0)

print(x_star)
print('done')
