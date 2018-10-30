# 绘制多组垂直和水平柱状图

import matplotlib.pyplot as plt
data = [[5,25,50,20],
        [4,34,65,13],
        [6,22,53,19]]
'''
plt.bar(range(4),data[0],width=0.25)
plt.bar([x + 0.25 for x in range(4)],data[1],width=0.25)
plt.bar([x + 0.5 for x in range(4)],data[2], width=0.25)
plt.show()
'''

plt.barh(range(4),data[0],height=0.25)
plt.barh([x + 0.25 for x in range(4)],data[1],height=0.25)
plt.barh([x + 0.5 for x in range(4)],data[2], height=0.25)
plt.show()
