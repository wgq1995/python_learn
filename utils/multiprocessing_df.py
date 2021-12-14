import numpy as np
import pandas as pd
import multiprocessing
from multiprocessing import Manager
import time

df = pd.DataFrame({
    'a': list(range(1000000)),
    'b': list(range(1000000)),
    'c': list(range(1000000)),
    'd': list(range(1000000))
})

def get_bucket_id(x, percents_values):
    if x <= 0:
        return 0
    l, r = 0, len(percents_values) - 1
    while l <= r:
        mid = (l + r) // 2
        if x == percents_values[mid]:
            return mid + 2
        elif x < percents_values[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return l + 1

def col_func(col_name, col_data, return_dict):
    quantile_values = np.linspace(0, 1, num=20, endpoint=False)[1:]
    percents_values = col_data.quantile(quantile_values).values
    new_series = col_data.map(lambda x: get_bucket_id(x, percents_values))
    return_dict[col_name] = new_series[:10].values

def driver(df):
    manager = Manager()
    # return_list = manager.list() 也可以使用列表list
    return_dict = manager.dict()
    jobs = []
    for col in df.columns:
        p = multiprocessing.Process(target=col_func, args=(col, df[col], return_dict))
        jobs.append(p)
        p.start()
    for proc in jobs:
        proc.join()
    return return_dict


if __name__ == '__main__':
    time1 = time.time()
    res1 = {}
    for col in df.columns:
        col_func(col, df[col], res1)
    print("串行耗时：%s" % (time.time() - time1))
    time1 = time.time()
    res2 = driver(df)
    print("并行耗时：%s" % (time.time() - time1))
    # 串行耗时：13.200478792190552
    # 并行耗时：3.622390031814575


