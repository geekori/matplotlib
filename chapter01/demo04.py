# 将文件作为数据源绘制曲线
import matplotlib.pyplot as plt
import numpy
'''
X,Y,Z = zip(*[[float(s) for s in line.split()]for line in open('data.txt', 'r')])
print(X)
print(Y)
print(Z)
plt.plot(X,Y)
plt.plot(X,Z)
plt.show()
'''

data = numpy.loadtxt('data.txt')
print(data.T)
for row in data.T:
    print(data[:,0])
    plt.plot(data[:,0],row)
plt.show()