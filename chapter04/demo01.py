'''

高级图表操作：在图表中绘制多组曲线

'''

import numpy
from matplotlib import pyplot as plot

T = numpy.linspace(-numpy.pi, numpy.pi,1024)
grid_size = (4,3)

# 占3行1列
plot.subplot2grid(grid_size,(0,0),rowspan=3,colspan=1)
plot.plot(numpy.sin(2 * T),numpy.cos(0.5 * T),c='r')

# 占3行2列
plot.subplot2grid(grid_size,(0,1),rowspan=3,colspan=2)
plot.plot(numpy.sin(3 * T),numpy.cos(T),c='b')

# 占1行3列
plot.subplot2grid(grid_size,(3,0),rowspan=1,colspan=3)
plot.plot(numpy.sin(5 * T),numpy.cos(7 * T),c='k')



# 让图尽量充满整个图表
plot.tight_layout()
plot.show()