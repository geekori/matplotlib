# 控制柱状图的填充模式
import numpy
import matplotlib.pyplot as plt
N = 8
A = numpy.random.random(N)
B = numpy.random.random(N)
plt.bar(range(N),A,color='b',hatch='x')
plt.bar(range(N),A+B,bottom=A,color='r',hatch='*')
plt.show()