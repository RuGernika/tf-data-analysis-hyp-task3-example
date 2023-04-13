import pandas as pd
import numpy as np
from scipy import stats

chat_id = 1902092480  # Ваш chat ID, не меняйте название переменной

def solution(data1: int, data2: int)-> bool:
  from scipy.stats import t

  mean1 = np.mean(data1)
  mean2 = np.mean(data2)
  std1 = np.std(data1, ddof=1)
  std2 = np.std(data2, ddof=1)
  n1 = len(data1)
  n2 = len(data2)
  t_stat = (mean1 - mean2) / np.sqrt((std1**2 / n1) + (std2**2 / n2))
  alpha = 0.04
  df = n1 + n2 - 2
  critical_value = t.ppf(1 - alpha, df)

  if t_stat > critical_value or t_stat < -critical_value:
    rez = 1
  else:
    rez = 0 
  return bool(rez)
