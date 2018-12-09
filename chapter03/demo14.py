'''

绘制tick线

Tick线又称闪电图、点线图，是在期货交易市场把每笔成交都列出显示的图形


'''

import numpy
import matplotlib.pyplot as plot
import matplotlib.ticker as ticker

X = numpy.linspace(-15,15,1024)
print(X)
# sinc(X)：具有与输入相同形态的值，sinc(0)是极限值
Y = numpy.sinc(X)
print(Y)

ax = plot.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

plot.plot(X,Y,c='r')
plot.show()

