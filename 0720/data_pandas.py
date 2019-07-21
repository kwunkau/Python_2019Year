import numpy as np
import pandas as pd
from scipy import stats

def weighted_avg(values, weights):
    return (values * weights).sum() / weights.sum()


if __name__ == '__main__':
    # 创建随机Series,10-20随机10个数
    # s = pd.Series(np.random.randint(10, 20, 10))

    df = pd.Series([2, 10, 60, 6, 5, 6])
    weights = pd.Series([1, 1, 2, 1, 1, 1])
    # 数据的集中程度
    print('中位数:', df.median())  # 中位数
    print('众数:',df.mode()[0])  # 众数
    print('极差:',df.max() - df.min())  # 极差
    print('分位数第一位',df.quantile(0.25))  # 25%分位数
    print('分位数第二位:',df.quantile(0.5))   # 50%分位数
    print('分位数第三位:',df.quantile(0.75))  # 75%分位数
    print('算术平均数:',df.mean())  # 平均数
    print('加权平均数:',weighted_avg(df, weights))  # 加权平均数
    print('加权平均数v2:', np.average(df,weights=weights))  # 加权平均数
    print('几何平均数', stats.gmean(df))
    print('-------------------------------')
    # 数据的离中趋势
    print('方差:',df.var())  # 方差
    print('标准差:',df.std())  # 标准差
    print('平均差:',np.abs(df-df.mean()).mean())  # 平均绝对偏差
    print('四分位极差:',df.quantile(0.75) - df.quantile(0.25))  # 四分位差
    print('异众比率:', 1 - df.value_counts()[df.mode()].sum() / df.count())
    print('-------------------------------')
    # 相对离散程度
    print('离散系数:',df.std() / df.mean())  # 离散系数
    print('-------------------------------')
    # 分布形态
    print('偏态系数:',df.skew())  # 偏度
    print('峰态系数:',df.kurt())  # 峰度
