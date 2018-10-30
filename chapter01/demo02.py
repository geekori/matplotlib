# 在数据可视化过程中使用NumPy

# 绘制正弦曲线（sin）


import math
import matplotlib.pyplot as plt
import numpy

'''
T = range(100)
X = [(2 * math.pi) * t / len(T) for t in T]
Y = [math.cos(value) for value in X]
print(X)
print('----------')
print(Y)
plt.plot(X,Y)
plt.show()
'''
X = numpy.linspace(0, 2 * numpy.pi, 100)
Y = numpy.sin(X)
plt.plot(X,Y)
plt.show()


