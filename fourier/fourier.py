import numpy as np


def integral(f, a, b):
    h = 0.001
    s = 0
    x_current = a

    while x_current < b:
        xi = x_current + h / 2
        s += f(xi) * h
        x_current += h

    return s


def fourier_tranformation(f, xi):
    finite_bound = 1
    def _f(x):
        return f(x) * np.exp(2*np.pi * 1j * x * xi)
    return integral(_f, -finite_bound, finite_bound)


# DoTo:
def fourier_tranformation_inverse(f, xi):
    pass


def fourier_coeff(f, T, N):
    a = np.empty(N+1, dtype=np.float)
    a[0] = (1 / T) * integral(f, 0, T)

    for i in range(N):
        def _f(t):
            return f(t) * np.cos((i+1) * (2*np.pi / T) * t)
        a[i+1] = (2 / T) * integral(_f, 0, T)

    b = np.empty(N, dtype=np.float)
    for i in range(N):
        def _f(t):
            return f(t) * np.sin((i+1) * (2*np.pi / T) * t)
        b[i] = (2 / T) * integral(_f, 0, T)

    return a, b


def calculate_fourier_series(t, a, b, T):
    N = len(b)
    f = a[0]

    cos = 0
    for n in range(1,N+1):
        cos += a[n] * np.cos(n * np.pi * 2 * t / T)
    f += cos

    sin = 0
    for n in range(1,N+1):
        sin += b[n-1] * np.sin(n * np.pi * 2 * t / T)
    f += sin

    return f
