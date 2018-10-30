# 在坐标系执行的位置添加注释

import numpy
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
X = numpy.linspace(-5,5,1024)
Y = .25 * (X + 4) * (X + 1) * (X - 2)
plt.text(-1,-0.3,'新的注释')
plt.plot(X,Y,c='b')
plt.show()