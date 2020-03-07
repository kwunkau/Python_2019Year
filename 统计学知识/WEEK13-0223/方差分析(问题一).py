#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "kau"
from scipy.stats import f
import pandas as pd
import numpy as np
'''
数据背景：有A、B、C、D四个地区，不同地区的销售量不一样，现抽取了不同时间段内每个地区的销售量，试解决：
1、每个地区间的销售量是否相同？
2、不同月份的销售量是否相同？
3、不同时间与地区的销售量是否相同？
https://mp.weixin.qq.com/s/6A-V4v9yGoT__Ja9er30bw
'''

data = pd.read_excel("销售数据.xlsx",index_col=0)
'''
提出原假设：
H0:u1=u2=u3=…=un，每个地区间的销售量没有显著变化。
H1:ui(i=1,2,3,…)不完全相等，地区对销量有显著变化。

1.计算平均值
'''
avg = data.mean().mean()
print('平均值(AVG)',avg)
# 2.计算总平方和
sst = ((data - avg)**2).sum().sum()
print('总平方和(SST):',sst)
# 3.计算组间平方和
SSA = 0
for col, colitems in data.iteritems():
  cnt = len(colitems)
  SSA += cnt*((colitems.mean() - avg)**2)

print('组间平方和(SSA):',SSA)

# 4.计算组内平方和
SSE = 0
for col, colitems in data.iteritems():
  col_mean = colitems.mean()
  SSE += ((colitems - col_mean)**2).sum()

print('组内平方和(SSE):',SSE)
'''
5.计算统计量
SST的自由度为n-1，其中n为全部观测值的个数。
SSA的自由度为k-1，其中k为因素水平（总体）的个数。
SSE的自由度为n-k。
'''
MSA = SSA/(len(data.columns)-1)
MSE = SSE/(data.size-len(data.columns))
F = MSA/MSE
print('服从F分布的统计量为:',F)

'''
6.统计决策

若去显著性水平0.05, F分布的临界值为：F阿法（3,40）
由于查的F阿法（3,40）=2.8387453980206443

结论：由于Fr>Fa 或者 P<0.05,属于小概率事件，拒绝原假设，即不同地区间的销售量存在显著差异。
'''
df1 = len(data.columns)-1
df2 = data.size-len(data.columns)
print(df1)
print(df2)
print(f.ppf(0.95, df1, df2))