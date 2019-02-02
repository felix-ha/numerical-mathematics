import numpy as np


if __name__ == '__main__':
    n = [1,0,0,0,0,0]

    n_ft = np.fft.fft(n)
    n_ft_inv = np.fft.ifft(n_ft)

    print('one dimensional fourier tranformation')
    print(n_ft)
    print(n_ft_inv)
    print()

    I = np.array([[0,0,0,0],
                    [0,1,1,0],
                    [0,1,1,0],
                    [0,0,0,0],])

    I_ft = np.fft.fft2(I)
    I_ft_inv = np.fft.ifft2(I_ft)

    print('two dimensional fourier tranformation')
    print(I_ft)
    print(I_ft_inv)
    print()
