# 绘制随机点

# scatter  plot

import random
import matplotlib.pyplot as plt
count = 1024
X = [random.random() * 100 for i in range(count)]
Y = [random.random() * 100for i in range(count)] 
print(X)
print(Y)

plt.scatter(X,Y)
plt.show()