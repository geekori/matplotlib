# 定制柱状图的颜色
import random
import matplotlib.pyplot as plt
values = [random.randint(0,99) for i in range(50)]
color_set = ['#FF00FF','#FFFF00','r','b']
color_list = [color_set[random.randint(0,3)] for i in range(50)]
plt.bar(range(len(values)),values,color=color_list)
plt.show()