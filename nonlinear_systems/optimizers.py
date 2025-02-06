# optimizers.py
import numpy as np

def gradient_descent(f, df, x0, learning_rate, tol, max_iter):
    x = x0.copy()
    errors = []
    for i in range(max_iter):
        grad = df(x)
        x -= learning_rate * grad
        errors.append(f(x))
        if np.linalg.norm(grad) < tol:
            break
    return x, errors

def newton_method(f, df, d2f, x0, max_iter, tol=1e-6):
    x = x0.copy()
    errors = []
    for i in range(max_iter):
        grad, hess = df(x), d2f(x)
        if np.linalg.det(hess) == 0:
            break
        delta = np.linalg.inv(hess) @ grad
        x -= delta
        errors.append(f(x))
        if np.linalg.norm(delta) < tol:
            break
    return x, errors