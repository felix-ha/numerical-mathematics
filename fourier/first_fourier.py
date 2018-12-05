import numpy as np
from matplotlib import pyplot as plt
plt.style.use('ggplot')


def ear(t):
    return 1.273*np.sin(2*np.pi * 128 * t) + 0.424*np.sin(2*np.pi * 384 * t)+ 0.255*np.sin(2*np.pi * 640 * t)

def f(x):
    return np.sin(x)


def rect(x):
    if x < 0:
        x = np.absolute(x) + np.pi

    if x > 2 * np.pi:
        n = int(x / (2 * np.pi))
        x = x - n * 2 * np.pi

    if 0 < x < np.pi:
        return 1
    elif x == 0 or x == np.pi or x == np.pi * 2:
        return 0
    else:
        return -1



def integral(f, a, b):
    h = 0.001
    s = 0
    x_current = a

    while x_current < b:
        xi = x_current + h / 2
        s += f(xi) * h
        x_current += h

    return s

def fourier(f, xi):
    def _f(x):
        return f(x) * np.exp(2*np.pi * 1j * x * xi)
    return integral(_f, -2, 2)

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


if __name__ == '__main__':
    N = 5
    f = rect

    n_a = range(N+1)
    n_b = range(N)

    T = 2 * np.pi
    a, b = fourier_coeff(f, T, N)

    x = np.arange(-10, 10, 0.001)
    f_x = [f(z) for z in x]
    f_fourier_series = [calculate_fourier_series(z, a, b, T) for z in x]

    plt.plot(x, f_x)
    plt.plot(x, f_fourier_series)
    plt.savefig('fourier.png', dpi=500)

    plt.plot(n_b, b)
    plt.show()





