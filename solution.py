import pandas as pd
import numpy as np
from scipy.stats import *

chat_id = 680977959 # Ваш chat ID, не меняйте название переменной
# data1 = pd.read_table('hyp3_historical_data.csv', sep=",", header=0, index_col=0)
# d1 = data1.to_numpy()
# print(data1)
def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    sta, p = ttest_ind(x, y)

    return p < 0.09
