# derivative.py
import numpy as np
def numerical_derivative(f, x, h=1e-6):
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_h = x.copy()
        x_h[i] += h
        grad[i] = (f(x_h) - f(x)) / h
    return grad