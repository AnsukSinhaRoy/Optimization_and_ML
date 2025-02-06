import numpy as np

def kaczmarz(A, b, x0, iterations, method='vanilla', step_size=0.01):
    m, n = A.shape
    x = x0.copy()
    error = np.zeros(iterations)
    
    if method == 'vanilla':
        for k in range(iterations):
            i = k % m
            ai, bi = A[i, :], b[i]
            x += step_size * (bi - ai @ x) / (np.linalg.norm(ai)**2) * ai
            error[k] = np.linalg.norm(A @ x - b)
    
    elif method == 'randomized':
        row_probs = np.sum(A**2, axis=1) / np.sum(A**2)
        for k in range(iterations):
            i = np.random.choice(m, p=row_probs)
            ai, bi = A[i, :], b[i]
            x += (bi - ai @ x) / (np.linalg.norm(ai)**2) * ai
            error[k] = np.linalg.norm(A @ x - b)
    
    return x, error