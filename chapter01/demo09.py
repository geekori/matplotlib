# 在同一个窗口绘制直方图和盒状图

import numpy as np
import matplotlib.pyplot as plt

# hist:直方图   hist(data,value)  data [ -1,1] value = 100
# boxplot：盒状图   boxplot(data)

# 
data = np.random.randn(100)
print(data)
print(np.average(data))

fig,(ax1,ax2),(ax3,ax4),(ax3,ax4) = plt.subplots(2,2,figsize=(8,8))
print(fig)
ax1.hist(data,100)
ax2.boxplot(data)
ax3.hist(data,50)
ax4.boxplot(data)
plt.show()








