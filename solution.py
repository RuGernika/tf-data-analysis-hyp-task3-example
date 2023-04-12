import pandas as pd
import numpy as np


chat_id = 1902092480  # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: 
    alpha = 0.04
    stat, pval  = ztest(x, value=500, alternative='larger')
    return pval < alpha. # Ваш ответ, True или False
