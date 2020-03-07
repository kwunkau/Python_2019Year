#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "kau"

import numpy as np
import pandas as pd
from scipy import stats

## 读取数据
df = pd.read_excel('data/1_table1.xlsx')  # 这个会直接默认读取到这个Excel的第一个表单

## 找出统计学成绩等于75的学生
df1 = df[df['统计学成绩'] == 75]
df2 = df.nlargest(3, columns='英语成绩')   # 英语成绩最高的前三名学生
df3 = df.nsmallest(3, columns='英语成绩')  # 英语成绩最低的前三名学生

## 找出四门课程成绩都大于70分的学生
df4 = df[(df['统计学成绩'] > 70) & (df['数学成绩'] > 70)
         & (df['英语成绩'] > 70) & (df['经济学成绩'] > 70)]

## 排序，ascending默认升序,ascending=False降序
df5 = df.sort_values(by='统计学成绩',ascending=False)

## 读取第二个sheet数据
ef = pd.read_excel('data/1_table1.xlsx',sheet_name=1)  # 这个会直接默认读取到这个Excel的第一个表单
## 透视表
ef2 = ef.pivot_table(index='性别', columns='家庭所在地区', values='平均月生活费(元)')

## count(计数、非空值)、mean（平均数）、std（标准差）
print(df.describe())

ff = df['统计学成绩']
print('中位数:', ff.median())  # 中位数
print('众数:',ff.mode()[0])  # 众数
print('极差:',ff.max() - ff.min())  # 极差
print('分位数第一位',ff.quantile(0.25))  # 25%分位数
print('分位数第二位:',ff.quantile(0.5))   # 50%分位数
print('分位数第三位:',ff.quantile(0.75))  # 75%分位数
print('算术平均数:',ff.mean())  # 平均数
print('几何平均数', stats.gmean(ff))
print('-------------------------------')
# 数据的离中趋势
print('方差:',ff.var())  # 方差
print('标准差:',ff.std())  # 标准差
print('平均差:',np.abs(ff-ff.mean()).mean())  # 平均绝对偏差
print('四分位极差:',ff.quantile(0.75) - ff.quantile(0.25))  # 四分位差
print('异众比率:', 1 - ff.value_counts()[ff.mode()].sum() / ff.count())
print('-------------------------------')
# 相对离散程度
print('离散系数:',ff.std() / ff.mean())  # 离散系数
print('-------------------------------')
# 分布形态
print('偏态系数:',ff.skew())  # 偏度
print('峰态系数:',ff.kurt())  # 峰度
