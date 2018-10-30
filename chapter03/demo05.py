# 设置文本注释的对齐方式
import matplotlib.pyplot as plt

align_list = ('center','left','right')
ax1 = plt.axes()
ax1.axes.get_xaxis().set_visible(False)
ax1.axes.get_yaxis().set_visible(False)
for i, align in enumerate(align_list):
    plt.text(0,i, 'align=\'%s\'' % align, ha=align)

plt.plot([0,0],[-1, len(align_list)],c='r', ls='--')
plt.scatter([0,0,0],range(len(align_list)))
plt.show()