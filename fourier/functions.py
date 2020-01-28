import numpy as np


def ear(t):
    return 1.273*np.sin(2*np.pi * 128 * t) + 0.424*np.sin(2*np.pi * 384 * t)+ 0.255*np.sin(2*np.pi * 640 * t)


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
