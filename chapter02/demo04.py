# 用颜色集合定制饼图的颜色
import random
import matplotlib.pyplot as plt
values  = [random.random() for i in range(15)]
color_set = ['r','b','y','0.5']
plt.pie(values,colors = color_set)
plt.show()