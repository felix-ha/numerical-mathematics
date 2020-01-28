import unittest
import numpy as np
from fourier.first_fourier import fourier_coeff

EPS = 1e-1


class TestFourierCoefficients(unittest.TestCase):
    def test_sin(self):


        x_rot_true = np.array([0,1,0,1])

        for i in range(4):
            self.assertLessEqual(abs(x_rot_true[i] - x_rot[i]), EPS)





if __name__ == '__main__':
    unittest.main()
