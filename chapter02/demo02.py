# 定制离散点的颜色、边缘颜色、边缘宽度和尺寸
import numpy
import matplotlib.pyplot as plt
A = numpy.random.standard_normal((100,2))
#print(A)
#print(A[:,0])

A += numpy.array((-1,-1))
B = numpy.random.standard_normal((100,2))
B += numpy.array((1,1))
colors =['red','yellow','b','c','#FF00FF','0.75']
plt.scatter(A[:,0],A[:,1],color=colors[0])
plt.scatter(B[:,0],B[:,1],color=colors[2])
plt.scatter(A[:,0],B[:,1],color=colors[4],edgecolor=colors[2],s=200,linewidths = 3)
plt.show()



