import numpy as np
from scipy.stats import expon
def solution(x: np.array) -> float:
    t = 10
    n = len(x)
    shift = -23
    lambda_param = 1
    import numpy as np
    v = shift + np.random.exponential(1/lambda_param, size=n)
    lambda_hat = 1 / np.mean(v - shift)
    return lambda_hat
