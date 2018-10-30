# 注释
# 01-在坐标系上显示标题（英文和中文）
import numpy
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
X = numpy.linspace(-4,4,1024)
Y = .25 * (X + 4) * (X + 1) * (X - 2)
plt.title('多项式曲线')
plt.plot(X,Y,c='r')
plt.show()