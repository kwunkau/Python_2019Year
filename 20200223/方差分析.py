#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "kau"

import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

'''
## https://mp.weixin.qq.com/s/6WOM6Qfw6-t-0CHPMFVRAw
1.提出原假设
H0:假设样本A,B,C,D的均值相同，不同地区无显著性影响
H1:假设样本A,B,C,D的均值不同，有显著性影响

3.因为每个时间段直接的存在明显差异，因此不同时间段和不同地区间的销量是存在差异的。
'''

#读取数据
data=pd.read_excel("销售数据.xlsx")
print(data.head())

#改列名
data=data.rename(columns={'Unnamed: 0':'date'})
columns=pd.Index(['A','B','C','D'],name='item')
data1=data.reindex(columns=columns)
data1.index=data['date']
data1=data1.stack().reset_index().rename(columns={0:'value'})
print(data1.head()) # 44行数据

'''
问题一：
按照α = 0.05，由此可看出：
Fr(3.466) > Fa 或者P(0.0249) <0.05，因此拒绝H0，地区对销售量有显著性影响
'''
formula='value~item'
model=ols(formula,data=data1).fit()
print(model.summary())

## 新增列求月份值及数据预处理
data1['month'] = data1['date'].dt.month

'''
问题二：
按照α = 0.05，由此可看出：
Fr(2.467) < Fa 或者P(0.124) > 0.05，因此原假设H0成立，月份对销售量没影响
'''
formula2='value~month'
model2=ols(formula2,data=data1).fit()
print(model2.summary())

model2_2= ols(formula2,data1).fit()
anovat=anova_lm(model2_2)
print(anovat)

'''
问题二：
按照α = 0.05，由此可看出：
1.地区：P(0.020985) <0.05，因此拒绝H0，地区对销售量有显著性影响
2.月份：P(0.094860) >0.05，因此不能拒绝H0，月份对销售量没显著性影响
'''

formula3='value~month + item'
model3=ols(formula3,data=data1).fit()
anovat3=anova_lm(model3)
print(anovat3)



