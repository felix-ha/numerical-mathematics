# numerical-mathematics

Implementations of different numerical algorithms in python. At the moment there is only GradientDescent available.

## Usage 

```python
import numpy as np
from nummath import GradientDescent


def f(x):
    return x[0]**2 + x[1]**2

x_0 = np.array([1,2])
result = GradientDescent(max_iterations=20000).optimize(f, x_0)
result.print()

```