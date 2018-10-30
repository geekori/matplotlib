# 在曲线上建立步长标记

import numpy
import matplotlib.pyplot as plt

X = numpy.linspace(-6,6,1024)
Y1 = numpy.sinc(X)  #辛格函数 sinc(x) = sin(x) * 1 / x 
Y2 = numpy.sinc(X) + 1

plt.plot(X,Y1, marker='x', color='r',markevery=50)
plt.plot(X,Y2, marker='o', color='b', markevery=32)
plt.show()