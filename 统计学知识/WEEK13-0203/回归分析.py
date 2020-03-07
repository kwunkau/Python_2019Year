#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "kau"

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor

# 加载数据集
data =  pd.read_csv('data.csv')
y = data.iloc[:,2]
x = data.iloc[:, 3:5]

# 拆分训练数据集和测试数据集
X_train, X_test, y_train, y_test = train_test_split(x, y,test_size = 0.25, random_state = 1)

# 数据归一化
standardScaler = StandardScaler()
standardScaler.fit(X_train)
X_train_standard = standardScaler.transform(X_train)
X_test_standard = standardScaler.transform(X_test)

# 实例化 SGDRegressor
sgd_reg = SGDRegressor(max_iter=1000, tol=1e-5)

# 对训练数据集进行拟合
sgd_reg.fit(X_train_standard, y_train)

print('coefficients(b1,b2...):',sgd_reg.coef_)
print('intercept(b0):',sgd_reg.intercept_)

# 预测数据
y_pred = sgd_reg.predict(X_test)
print(y_pred)

# 对测试数据集进行评分
print('模型评分：', sgd_reg.score(X_test_standard, y_test))


