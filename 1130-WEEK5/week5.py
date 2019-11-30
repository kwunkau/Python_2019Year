#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "kau"

import pandas as pd
'''
数据关于体温、性别、心率的临床数据，并对以下问题进行数据分析：

1.人类体温均值真的是98.6F吗？
2.体温样本数据是否服从正态分布？
3.不正常的体温是多少？
4.男性和女性的正常体温有明显的区别吗？
5.体温和心率是否有相关性？
'''

datadf = pd.read_csv('http://jse.amstat.org/datasets/normtemp.dat.txt',header=None,sep='\s+',names=['体温','性别','心率'])
print(datadf.describe())
## 问题1结论：可以看到 体温的均值为 98.25 F

