# 绘制多条曲线
import numpy
import matplotlib.pyplot as plt

X = numpy.linspace(-3,3,200)
Y = X**2 - 2 * X + 1
plt.plot(X,Y)

X = numpy.linspace(0, 2 * numpy.pi, 100)
Ya = numpy.sin(X)
Yb = numpy.cos(X)
plt.plot(X,Ya)
plt.plot(X,Yb)
plt.show()



