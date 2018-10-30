# 定制盒装图每一部分的颜色

import random 
import matplotlib.pyplot as plt

# 0：平均值   1：标准差
values = [random.gauss(0,1) for i in range(100)]
print(values)
b = plt.boxplot(values)
colorList = ['r','b','g','y']
i = 0
for name, line_list in b.items():
    color = colorList[i % len(colorList)]
    i += 1
    for line in line_list:
        line.set_color(color)
    
plt.show()