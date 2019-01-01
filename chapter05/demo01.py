'''
将图表保存为png图像


'''
import numpy
import matplotlib.pyplot as plt

X = numpy.linspace(-6,6,1024)
Y= numpy.sinc(X)
# 用于子图表的X
X_detail = numpy.linspace(-3,3,1024)
# 用于子图表的Y
Y_detail = numpy.sinc(X_detail)

plt.plot(X,Y,c='b')
# 放置一个子图表
# [0.6,0.6,0.25,0.25] 中的值是占图表水平或垂直的宽度和高度
sub_axes = plt.axes([0.6,0.6,0.25,0.25])
# 在子图表中绘制曲线
sub_axes.plot(X_detail, Y_detail,c='r')

# 必须在调用show函数之前调用，否则不会成功保存图表
plt.savefig('pic1.png')
plt.show()



