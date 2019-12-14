import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

'''
参考：https://www.jianshu.com/p/6522cd0f4278
数据集描述：数据包括【ID、年龄、价格、港口】
问题1：按照港口分类，使用Python求出各类数据年龄和价格的统计量（方差、均值等）
问题2：画出价格的分布图像，验证数据服从何种分布（卡方？正态？T分布？）
问题3：按照港口分类，验证S港与Q港两个港口之间的平均价格之差是否服从某种分布？
'''

df = pd.read_excel("data/data.xlsx")
# 按照港口分类，计算数据的统计量
print(df.groupby(['Embarked']).describe())

'''
1.1、 画出年龄的分布图像，验证数据服从何种分布（正态？卡方？还是T?）
画出年龄的图像
'''
sns.set_palette("hls")  # 设置所有图的颜色，使用hls色彩空间
sns.distplot(df['Age'], color="r", bins=10, kde=True)
plt.title('Age')
plt.xlim(-10, 80)
plt.grid(True)
plt.show()


'''
1.2、验证是否服从正态分布?
分别用kstest、shapiro、normaltest来验证分布系数
结论：由于P<0.05,不服从正态分布
'''
ks_test = stats.kstest(df['Age'], 'norm')
shapiro_test = stats.shapiro(df['Age'])
normaltest_test = stats.normaltest(df['Age'],axis=0)

print('ks_test:',ks_test)
print('shapiro_test:',shapiro_test)
print('normaltest_test:',normaltest_test)

'''
1.3、绘制拟合正态分布曲线
'''

age = df['Age']
plt.figure()
age.plot(kind = 'kde')   #原始数据的正态分布
M_S = stats.norm.fit(age)  #正态分布拟合的平均值loc，标准差 scale
normalDistribution = stats.norm(M_S[0], M_S[1])  # 绘制拟合的正态分布图
x = np.linspace(normalDistribution.ppf(0.01), normalDistribution.ppf(0.99), 100)
plt.plot(x, normalDistribution.pdf(x), c='orange')
plt.xlabel('Age about Titanic')
plt.title('Age on NormalDistribution', size=20)
plt.legend(['age', 'NormDistribution'])
plt.show()

'''
2.2 验证是否服从T分布？
'''
np.random.seed(1)
ks = stats.t.fit(age)
df = ks[0]
loc = ks[1]
scale = ks[2]
ks2 = stats.t.rvs(df=df, loc=loc, scale=scale, size=len(age))
print(stats.ks_2samp(age, ks2))

'''
2.3 由检验结果知,p <0.05，所以拒绝原假设，认为数据不服从T分布
绘制拟合的T分布图
'''

plt.figure()
age.plot(kind = 'kde')
TDistribution = stats.t(ks[0], ks[1],ks[2])
x = np.linspace(TDistribution.ppf(0.01), TDistribution.ppf(0.99), 100)
plt.plot(x, TDistribution.pdf(x), c='orange')
plt.xlabel('Age about Titanic')
plt.title('Age on TDistribution', size=20)
plt.legend(['age', 'TDistribution'])
plt.show()

'''
3.2 验证数据是否服从卡方分布
'''
np.random.seed(1)
chi_S = stats.chi2.fit(age)
df_chi = chi_S[0]
loc_chi = chi_S[1]
scale_chi = chi_S[2]
x2 = stats.chi2.rvs(df=df_chi, loc=loc_chi, scale=scale_chi, size=len(age))
print(stats.ks_2samp(age, x2))

'''
3.3 对数据进行卡方拟合
'''

plt.figure()
age.plot(kind = 'kde')
chiDistribution = stats.chi2(chi_S[0], chi_S[1],chi_S[2])  # 绘制拟合的正态分布图
x = np.linspace(chiDistribution.ppf(0.01), chiDistribution.ppf(0.99), 100)
plt.plot(x, chiDistribution.pdf(x), c='orange')
plt.xlabel('age about Titanic')
plt.title('age on chi-square_Distribution', size=20)
plt.legend(['age', 'chi-square_Distribution'])
plt.show()