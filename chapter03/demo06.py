# 设置文本注释的对齐方式
import matplotlib.pyplot as plt

align_list = ('center','bottom','top','baseline')

for i, align in enumerate(align_list):
    plt.text(3 * i,0, 'align=\'%s\'' % align, va=align)

plt.plot([-3,3 * len(align_list)],[0,0],c='r', ls='--')
plt.scatter([3 * i for i in range(len(align_list))],[0,0,0,0])
plt.show()