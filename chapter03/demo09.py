'''

添加图例

'''

import numpy
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False
X = numpy.linspace(0,6,1024)
Y1 = numpy.sin(X)
Y2 = numpy.cos(X)
plt.xlabel('X')
plt.ylabel('Y')

plt.plot(X,Y1, c = 'r',lw = 3,label='sin(X)')
plt.plot(X,Y2, c = 'b',lw = 3,label='cos(X)')

# 显示图例

plt.legend(loc='right',fancybox=True,shadow=False,title='正弦和余弦',ncol=2)
plt.show()
