import pandas as pd
import numpy as np
import os
from scipy import stats

'''
尝试解决以下问题：
人类体温均值真的是98.6F吗？
体温样本数据是否服从正态分布？
不正常的体温是多少？
男性和女性的正常体温有明显的区别吗？
体温和心率是否有相关性？
'''

data = pd.read_csv('test.csv',header=None,names=['Temperature','Gender','HeartRate'])
print(data.describe())

# 计算置信区间温度的置信区间：
tem = data[["Temperature"]]

def interval(data, alpha=0.05):
    mean = np.mean(data)
    std = np.std(data)
    interval = stats.norm.interval(1 - alpha, mean, std)
    return interval

print(interval(tem))
'''
(array([96.81775583]), array([99.68070571]))
1.可以看到98.6在置信区间内。
'''

u = data['Temperature'].mean()  # 计算均值
std = data['Temperature'].std()  # 计算标准差
ks_test = stats.kstest(data['Temperature'], 'norm', (u, std))
print(ks_test)
shapiro_test = stats.shapiro(data['Temperature'])
print(shapiro_test)
normaltest_test = stats.normaltest(data['Temperature'], axis=None)
print(normaltest_test)
'''
KstestResult(statistic=0.06472685044046644, pvalue=0.6450307317439967)
(0.9865769743919373, 0.2331680953502655)
NormaltestResult(statistic=2.703801433319236, pvalue=0.2587479863488212)
'''
'''2.从以上三种方法的检验结果来看符合正态分布'''
# 计算上下四分位数
Q1 = data['Temperature'].quantile(q=0.25)
Q3 = data['Temperature'].quantile(q=0.75)
print(Q1)
print(Q3)
# 异常值判断标准， 1.5倍的四分位差 计算上下须对应的值
low_quantile = Q1 - 1.5 * (Q3 - Q1)
high_quantile = Q3 + 1.5 * (Q3 - Q1)

print(low_quantile)
print(high_quantile)
# 输出异常值
value = data['Temperature'][(data['Temperature'] > high_quantile) | (data['Temperature'] < low_quantile)]
print(value)
'''
97.8
98.7
96.44999999999999
100.05000000000001
0       96.3
65      96.4
129    100.8
'''
'''3.以上输出就为箱型图方法判断的异常值'''
# 首先剔除全部的异常值
data2 = data.loc[(data['Temperature'] != 96.3) & (data['Temperature'] != 96.4) & (data['Temperature'] != 100.8)]
data3 = data2.loc[data2['Gender'] == 1]
man_mean_temperature = data3['Temperature'].mean()
print(man_mean_temperature)
data4 = data2.loc[data2['Gender'] == 2]
woman_mean_temperature = data4['Temperature'].mean()
print(woman_mean_temperature)
'''
98.13281250000003
98.38730158730158
'''
miaoshu = data.groupby('Gender')["Temperature"].describe()
print(miaoshu)
male_tem = data.query(" Gender > 1")["Temperature"]
fmale_tem = data.query(" Gender < 2")["Temperature"]
# 检验是否是齐方差
print(stats.levene(male_tem, fmale_tem))
# 方差齐的情况下，可以使用ttst_ind(a,b)来做假设检验的：
print(stats.ttest_ind(male_tem, fmale_tem))
'''
        count       mean       std   min   25%   50%   75%    max
Gender
1        65.0  98.104615  0.698756  96.3  97.6  98.1  98.6   99.5
2        65.0  98.393846  0.743488  96.4  98.0  98.4  98.8  100.8
LeveneResult(statistic=0.06354951292025163, pvalue=0.8013756068102883)
Ttest_indResult(statistic=2.2854345381654984, pvalue=0.02393188312240236)
'''
'''4.从结果来看，可以接受齐方差，拒绝均值相等。即男女体温均值有差异。'''
print(data2.corr())
print(data2.corr('kendall'))
print(data2.corr('spearman'))
'''
             Temperature    Gender  HeartRate
Temperature     1.000000  0.192293   0.243285
Gender          0.192293  1.000000   0.054193
HeartRate       0.243285  0.054193   1.000000
             Temperature    Gender  HeartRate
Temperature     1.000000  0.159488   0.176732
Gender          0.159488  1.000000   0.064551
HeartRate       0.176732  0.064551   1.000000
             Temperature    Gender  HeartRate
Temperature     1.000000  0.190609   0.265460
Gender          0.190609  1.000000   0.077409
HeartRate       0.265460  0.077409   1.000000
'''
'''5.从上述三种系数来看，心率与体温呈现弱相关性'''