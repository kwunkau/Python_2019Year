#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm

'''
https://www.jianshu.com/p/fcf322fb48ad
数据背景:
03年到19年第一季度分季度的数据，13年之前只有传统汽车的销量，13年之后是传统汽车+新能源汽车的销量，需要预测未来三期传统汽车的销量～
ps:传统汽车的销量会受到新能源汽车的影响噢~
'''

df = pd.read_excel(r'时序数据.xlsx',index_col=0)
df.index.name =None
df.reset_index(inplace=True)
df.drop(df.index[64], inplace=True)
start = datetime.datetime.strptime("2003-01", "%Y-%m")# 把一个时间字符串解析为时间元组
# 从2003-01-01开始逐月增加组成list
date_list = [start + relativedelta(months=x*3)for x in range(0, 64)]

df['index'] = date_list
df.set_index(['index'], inplace=True)
print(df.head())

#先看传统汽车整体趋势：
dta = np.array(df['传统汽车销量'], dtype=np.float)
# 生成时间序列并画图
dta = pd.Series(dta)
dta.index = df.index

# 趋势
dta.plot(figsize=(12, 8), title='Monthly Total Traditional Car')
plt.show()


#有明显的递增趋势，可以判断是非平稳的，再来看看是否有季节性：
decomposition = seasonal_decompose(df['传统汽车销量'], freq=12)
fig = plt.figure()
fig = decomposition.plot()
fig.set_size_inches(15, 8)
plt.show()


#可以看到有明显季节性波动，需要将数据平稳化，这里我用简单的二阶差分进行（这里可以配合季节性差分进行测试（shift(12) ），最终选择差分方式）
fig = plt.figure(figsize=(12, 8))
ax2 = fig.add_subplot(111)
diff2 = dta.diff(2)
diff2.plot(ax=ax2)
plt.show()

## 接下来寻找最优p，q值组合：
adfuller(diff2[2:])
arma_mod70 = sm.tsa.ARMA(dta, (7, 0)).fit()
print(arma_mod70.aic, arma_mod70.bic, arma_mod70.hqic)
arma_mod30 = sm.tsa.ARMA(dta, (0, 1)).fit()
print(arma_mod30.aic, arma_mod30.bic, arma_mod30.hqic)
arma_mod80 = sm.tsa.ARMA(dta, (8, 0)).fit()
print(arma_mod80.aic, arma_mod80.bic, arma_mod80.hqic)

#最后可以进行预测了

predict_dta = arma_mod80.predict('2019', '2021', dynamic=True)
print(predict_dta)
fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.ix['2000':].plot(ax=ax)
fig = arma_mod80.plot_predict('2019', '2021', dynamic=True, ax=ax, plot_insample=False)
plt.show()


#对拟合效果进行评估
tempModel = sm.tsa.ARMA(dta, (8, 0)).fit()
delta = tempModel.fittedvalues - dta
score =1 - delta.var()/dta.var()
print("评估分数为:",score)