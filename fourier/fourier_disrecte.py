import numpy as np


def dft(n):
    N = len(n)
    ft = np.empty(N, dtype=complex)
    for k in range(N):
        tmp = 0
        for j in range(N):
            tmp += np.exp(-2 * np.pi * 1j * j * k / N) * n[j]
        ft[k] = tmp
    return ft

def idft(n):
    N = len(n)
    ft = np.empty(N, dtype=complex)
    for k in range(N):
        tmp = 0
        for j in range(N):
            tmp += np.exp(2 * np.pi * 1j * j * k / N) * n[j]
        ft[k] = tmp
    return 1/N * ft

if __name__ == '__main__':
    n = [1,0,0,0,0,5]

    n_ft = np.fft.fft(n)
    n_ft_inv = np.fft.ifft(n_ft)

    print('one dimensional fourier tranformation')
    print(n_ft)
    print(dft(n))
    print(idft(dft(n)))
    # print(n_ft_inv)
    # print()

    I = np.array([[0,0,0,0],
                    [0,1,1,0],
                    [0,1,1,0],
                    [0,0,0,0],])

    I_ft = np.fft.fft2(I)
    I_ft_inv = np.fft.ifft2(I_ft)

    # print('two dimensional fourier tranformation')
    # print(I_ft)
    # print(I_ft_inv)
    # print()
