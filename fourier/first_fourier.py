import numpy as np
from functions import rect, ear
from fourier import fourier_coeff, calculate_fourier_series, fourier_tranformation
from matplotlib import pyplot as plt
plt.style.use('ggplot')

def fourier_series_rect():
    N = 10
    f = rect

    T = 2 * np.pi
    a, b = fourier_coeff(f, T, N)

    x = np.arange(-10, 10, 0.001)
    f_x = [f(z) for z in x]
    f_fourier_series = [calculate_fourier_series(z, a, b, T) for z in x]


    plt.subplot(2,1,1)
    plt.plot(x, f_x)
    plt.plot(x, f_fourier_series)
    plt.legend(['f', 'f series of f'])
    plt.title('function vs fourier series')


    #plot coeff

    plt.subplot(2,1,2)
    n_a = range(N+1)
    n_b = range(N)

    plt.plot(n_a, a)
    plt.plot(n_b, b)
    plt.legend(['a', 'b'])
    plt.title('fourier coeffiecents')



    plt.savefig('fourier.png', dpi=500)
    plt.show()


def fourier_transormation_rect():
    f = rect

    x = np.arange(-6, 6, 0.01)
    x_trafo = np.arange(-15, 15, 0.01)
    f_x = [f(z) for z in x]
    f_fourier_trafo = [fourier_tranformation(f, z) for z in x_trafo]

    plt.subplot(2,1,1)
    plt.plot(x, f_x)
    plt.title('function')
    plt.ylim([-1.5, 1.5])


    plt.subplot(2,1,2)
    plt.plot(x_trafo, np.real(f_fourier_trafo))
    plt.plot(x_trafo, np.imag(f_fourier_trafo))
    plt.title('fourier transformation')
    plt.legend(['real', 'imag'])



    plt.savefig('fourier_transform.png', dpi=500)
    plt.show()



if __name__ == '__main__':
    fourier_series_rect()
    fourier_transormation_rect()





