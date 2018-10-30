# 使用colormap定制离散点的颜色
import numpy
import matplotlib.cm as cm
import matplotlib.pyplot as plt

N = 256
angle = numpy.linspace(0,8 * 2 * numpy.pi,N)
radius = numpy.linspace(0.5,1,N)

X = radius * numpy.cos(angle)
Y = radius * numpy.sin(angle)

plt.scatter(X,Y,c = angle,cmap=cm.hot)
plt.show()