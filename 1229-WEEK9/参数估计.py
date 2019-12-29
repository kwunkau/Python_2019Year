import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_excel("../1214-WEEK7/data/data.xlsx")
age = data['Age']
# print(age.describe())       ## mean：29.642093
age_sam = age.sample(100)   ## 抽取100个样本
# print(age_sam.describe())   ## mean：27.162500

'''
2、计算置信区间
1)、pandas.std() 默认是除以n-1 的，即是无偏的，如果想和numpy.std() 一样有偏，需要加上参数ddof=0 ，即pandas.std(ddof=0) ；DataFrame的describe()中就包含有std()；
2）、 numpy.std() 求标准差的时候默认是除以 n 的，即是有偏的，np.std无偏样本标准差方式为加入参数 ddof = 1
'''

#总体方差未知 使用样本方差
def norm_conf1 (data,confidence=0.95):
    sample_mean = np.mean(data)
    sample_std = np.std(data,ddof=1)
    sample_size = len(data)
    conf_intveral = stats.norm.interval(confidence, loc=sample_mean, scale=sample_std)
    print(conf_intveral)

#总体方差已知 Overall_std
def norm_conf2 (data,std_n,confidence=0.95):
    sample_mean = np.mean(data)
    sample_size = len(data)
    conf_intveral = stats.norm.interval(confidence, loc=sample_mean, scale=std_n)
    print(conf_intveral)


'''计算T分布下的置信区间'''
#总体方差未知
def ttest_conf1 (data,confidence=0.95):
    sample_mean = np.mean(data)
    sample_std = np.std(data,ddof=1)
    sample_size = len(data)
    conf_intveral = stats.t.interval(confidence,df = (sample_size-1) , loc=sample_mean, scale=sample_std)
    print(conf_intveral)

#总体方差已知
def ttest_conf2 (data,std_n,confidence=0.95):
    sample_mean = np.mean(data)
    sample_std = np.std(data,ddof=1)
    sample_size = len(data)
    conf_intveral = stats.t.interval(confidence,df = (sample_size-1) , loc=sample_mean, scale=std_n)
    print(conf_intveral)

norm_conf1 (age_sam)
ttest_conf1(age_sam)

'''重复抽取数据,大样本条件下'''
scale_means = []
for _ in range(1000):
   scale_sample = age.sample(100, replace=True)
   mean = scale_sample.mean()
   scale_means.append(mean)

norm_conf1 (scale_means)
ttest_conf1(scale_means)


sns.set_palette("hls") #设置所有图的颜色，使用hls色彩空间
sns.distplot(scale_means,color="r",bins=10,kde=True)
plt.title('Age')
plt.xlim(25,35)
plt.grid(True)
plt.show()
