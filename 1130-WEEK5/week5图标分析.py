#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "kau"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
# 有中文出现的情况，需要u'内容'


df = pd.read_csv('http://jse.amstat.org/datasets/normtemp.dat.txt',header=None,sep='\s+',names=['体温','性别','心率'])

## 三点图
fig = plt.figure(figsize=(16, 5))
plt.scatter(df['性别'], df['体温'], c='b', marker='o', alpha=0.7)
plt.title('散点图')
plt.xlabel('性别')
plt.ylabel('体温')
plt.grid(True)
plt.show()

plt.scatter(df['心率'], df['体温'], c='b', marker='<', alpha=0.7)
plt.title('散点图')
plt.xlabel('心率')
plt.ylabel('体温')
plt.grid(True)
plt.show()

## 柱形图
x = np.arange(0, 130, 1)
y = df['体温'].values
plt.bar(x, y)
plt.show()

## 直方图
df['体温'].hist(bins=20, alpha=0.5)
plt.show()

## 密度直方图
df['体温'].hist(bins=20, alpha=0.5)
df['体温'].plot(kind='kde', secondary_y=True)
plt.show()

'''
## 用python为直方图绘制拟合曲线，使用seaborn中的displot绘制
## 设置详细的参数，可采用kde_kws(拟合曲线的设置)，hist_kws(直方图柱子的设置)

import seaborn as sns
import matplotlib as mpl
sns.set_palette("hls")  # 设置所有图的颜色，使用hls色彩空间
sns.distplot(df['体温'], color="r", bins=30, kde=True)
plt.show()

## lw为曲线的粗细程度
sns.set_palette("hls")
mpl.rc("figure", figsize=(6, 4))
sns.distplot(df['体温'], bins=30, kde_kws={"color": "seagreen", "lw": 3}, hist_kws={"color": "b"})
plt.show()

'''

