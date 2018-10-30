# 定制颜色和样式

# 01-定制曲线的颜色

'''
1. 预定义颜色
b Blue
g Green
r Red
c Cyan（青色）
m Magenta（品红色）
y Yellow
k Black
w White
2. HTML颜色

#FF00FF

3. 灰度
用介于0到1之间的浮点数表示
0表示黑色   1表示白色
'''
import numpy
import matplotlib.pyplot as plt
X = numpy.linspace(-6,6,1024)
colors =['red','yellow','b','c','#FF00FF','0.75']
for i in range(20):
    plt.plot(X,-X**2 + (i+1)*2,color=colors[i % len(colors)])
plt.show()