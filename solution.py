import pandas as pd
import numpy as np


chat_id = 416934694 # Ваш chat ID, не меняйте название переменной

import numpy as np
from scipy.stats import expon
def solution(x: np.array) -> float:
    t = 10
    n = len(x)
    mu=-23
    sigma = np.exp(1)
    v = expon.rvs(mu,sigma,n)
    a = v/t
    return 1/a.mean()
