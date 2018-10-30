# 绘制三角剖分
import random
import matplotlib.pyplot as plt
import matplotlib.tri as tri
'''
count = 4
X = [1,2,3,4]
Y = [1,5,0,1]

'''
count = 100
X = [random.random() * 20 for i in range(count)]
Y = [random.random() * 2 for i in range(count)]
triangles = tri.Triangulation(X,Y)
plt.triplot(triangles,'r--')
plt.show()




