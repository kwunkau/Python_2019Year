# 案例：玩抛硬币的游戏，只抛1次硬币，成功抛出正面朝上记录为1，反面朝上即抛硬币失败记录为0

# 导入包
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pylab import mpl
# 解决jupyter 中文问题
mpl.rcParams['font.sans-serif'] = ['SimHei']
'''
第1步，定义随机变量：1次抛硬币
正面朝上记录为1，反面朝上记录为0
'''
# arange用于生成一个等差数组，arange([start, ]stop, [step, ]
X1 = np.arange(0,2,1)
print(X1)

'''
第2步，求对应分布的概率：概率质量函数（PMF）
返回一个列表，列表中每个元素表示随机变量中对应值的概率
'''
p1 = 0.5 # 硬币朝上的概率
pList1 = stats.bernoulli.pmf(X1,p1)
print(pList1)

'''
第3步，绘图
plot默认绘制折线
marker：点的形状，值o表示点为圆圈标记（circle marker）
linestyle：线条的形状，值None表示不显示连接各个点的折线
'''
plt.plot(X1,pList1,marker='o',linestyle='None')

'''
vlines用于绘制竖直线(vertical lines),
参数说明：vline(x坐标值, y坐标最小值, y坐标值最大值)
我们传入的X是一个数组，是给数组中的每个x坐标值绘制竖直线，
竖直线y坐标最小值是0，y坐标值最大值是对应pList1中的值
'''
plt.vlines(X1,0,pList1)
plt.xlabel('随机变量：抛1次硬币')
plt.ylabel('概率')
plt.title('伯努利分布：p=%.2f' % p1)
plt.show()
