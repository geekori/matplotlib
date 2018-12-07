'''

为坐标系添加网格

'''

import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-4,4,1024)
Y = 0.25 * (X + 6.0) * (X + 1.0) * (X - 2.0)

plot.plot(X,Y,c='b')
plot.grid(True,lw=2,ls='--',c='0.5')
plot.show()