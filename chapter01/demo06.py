# 绘制垂直和水平柱状图

# bar barh

import matplotlib.pyplot as plt
# bar(X,Y)
data = [30,53,12,45]
# X = [0,1,2,3]
#plt.bar(range(len(data)), data)
plt.bar([1980,1985,1990,1995],[1000,3000,4000,5000],width = 3)
#plt.show()
#plt.barh(range(len(data)), data)
#plt.barh([1980,1990,1994,1997],[1000,3000,4000,5000],height = 2)
plt.show()

