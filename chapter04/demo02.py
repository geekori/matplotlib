'''

设置坐标范围

'''

import numpy
import matplotlib.pyplot as plt

X = numpy.linspace(-6,6,1024)
plt.xlim(-20,20)
plt.ylim(-1,1.5)
plt.plot(X,numpy.sinc(X),c='r')   # 辛格函数
plt.show()