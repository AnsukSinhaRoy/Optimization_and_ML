# cost_functions.py
import numpy as np
def least_squares_cost(w, X, y):
    return 0.5 * np.mean((X @ w - y) ** 2)

def logistic_cost(w, X, y):
    preds = 1 / (1 + np.exp(-X @ w))
    preds = np.clip(preds, 1e-6, 1 - 1e-6)
    return -np.mean(y * np.log(preds) + (1 - y) * np.log(1 - preds))