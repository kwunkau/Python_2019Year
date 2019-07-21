#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd

def weighted_avg(values, weights):
    return (values * weights).sum() / weights.sum()

if __name__ == '__main__':
    df = pd.Series([2, 10, 60, 6, 5, 6])
    weights = pd.Series([1, 1, 2, 1, 1, 1])
    # 数据的集中程度
    print(df.median())  # 中位数
    print(df.mode())  # 众数
    print(df.max() - df.min())  # 极差
    print(df.quantile(0.25))  # 25%分位数
    print(df.quantile(0.5))   # 50%分位数
    print(df.quantile(0.75))  # 75%分位数
    print(df.mean())  # 平均数
    print(weighted_avg(df, weights))  # 加权平均数
    print('-------------------------------')
    # 数据的离中趋势
    print(df.var())  # 方差
    print(df.std())  # 标准差
    print(df.mad())  # 平均绝对偏差
    print(df.quantile(0.75) - df.quantile(0.25))  # 四分位差
    print('-------------------------------')

    # 相对离散程度
    print(df.std() / df.mean())  # 离散系数
    print('-------------------------------')
    # 分布形态
    print(df.skew())  # 偏度
    print(df.kurt())  # 峰度
