'''

设置图标的长宽比

'''


import numpy
import matplotlib.pyplot as plt

X = numpy.linspace(-6,6,1024)
Y1,Y2 = numpy.sinc(X),numpy.cos(X)
# 改变图标的宽度
plt.figure(figsize=(10,4))  # 英寸
plt.ylim(-0.5 * numpy.pi, 0.5 * numpy.pi)
plt.plot(X,Y1,c='b',lw=3)
plt.plot(X,Y2,c='r',lw=3)
plt.show()
