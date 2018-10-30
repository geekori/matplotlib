#  绘制叠加的柱状图

import matplotlib.pyplot as plt

A = [5,30,45,22]
B = [5,25,50,20]
'''

X = range(4) # [0,1,2,3]
plt.bar(X, A,color='b')
plt.bar(X, B,color='r',bottom=A)
plt.show()
'''
import numpy
data = numpy.array([[5,30,45,22],
                   [5,25,50,20],
                   [10,4,5,2]])
color_list=['b','g','r']
print(data.shape[1])
X = numpy.arange(data.shape[1])
for i in range(data.shape[0]):
    print(data[:i])
    S = numpy.sum(data[:i],axis = 0)
    plt.bar(X,data[i],bottom=S,color=color_list[i%len(color_list)])
plt.show()

