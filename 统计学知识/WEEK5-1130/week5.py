#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "kau"
from scipy import stats
import pandas as pd
'''
数据关于体温、性别、心率的临床数据，并对以下问题进行数据分析：

1.人类体温均值真的是98.6F吗？
2.体温样本数据是否服从正态分布？
3.不正常的体温是多少？
4.男性和女性的正常体温有明显的区别吗？
5.体温和心率是否有相关性？
'''

df = pd.read_csv('http://jse.amstat.org/datasets/normtemp.dat.txt',header=None,sep='\s+',names=['体温','性别','心率'])
print(df.describe())
## 问题1结论：可以看到 体温的均值为 98.25 F
'''
2. 体温样本数据是否服从正态分布？
检测体温是否服从正态分布:以下分别使用 kstest、shapiro、normaltest三种方法来检验。
结论:三种检验的pvalue值均大于5%，因此体温值服从正态分布。
'''
u = df['体温'].mean()  # 计算均值
std = df['体温'].std()  # 计算标准差
ks_test = stats.kstest(df['体温'], 'norm',(u,std))
print(ks_test)

shapiro_test = stats.shapiro(df['体温'])
print(shapiro_test)

normaltest_test = stats.normaltest(df['体温'], axis=None)
print(normaltest_test)

'''
3. 不正常的体温是多少？
结论：体温值大于100.05F，小于96.45F的均为异常体温。
'''
# 计算上下四分位数
Q1 = df['体温'].quantile(q = 0.25)  #97.8
Q3 = df['体温'].quantile(q = 0.75)  #98.7

#异常值判断标准， 1.5倍的四分位差 计算上下须对应的值
low_quantile = Q1 - 1.5*(Q3-Q1)   #96.44999999999999
high_quantile = Q3 + 1.5*(Q3-Q1)  #100.05000000000001

# 输出异常值
value = df['体温'][(df['体温'] > high_quantile) | (df['体温'] < low_quantile)]
print(value)

'''
4. 男性和女性的正常体温有明显的区别吗？
剔除异常体温后，分析样本中男女体温是否有明显区别
结论:女性体温均值比男性体温均值偏高
'''
df2 = df.loc[(df['体温'] != 96.3)&(df['体温'] != 96.4)&(df['体温'] != 100.8)]  #排除异常值
df3 = df2.loc[df2['性别']==1]
man_narmal_mean_temperature = df3['体温'].mean() #男士体温均值 98.13281250000003
df4 = df2.loc[df2['性别']==2]
woman_narmal_mean_temperature = df4['体温'].mean()#女士体温均值 98.38730158730158

'''
5. 体温和心率是否有相关性？
结论：由上面三种相关系数可以看出 心率和体温具有正相关
'''

df2.corr()
'''
          体温        性别        心率
体温  1.000000  0.192293  0.243285
性别  0.192293  1.000000  0.054193
心率  0.243285  0.054193  1.000000
'''
df2.corr('kendall')
'''
          体温        性别        心率
体温  1.000000  0.159488  0.176732
性别  0.159488  1.000000  0.064551
心率  0.176732  0.064551  1.000000
'''

df2.corr('spearman')
'''
         体温        性别        心率
体温  1.000000  0.190609  0.265460
性别  0.190609  1.000000  0.077409
心率  0.265460  0.077409  1.000000
'''