'''

动态产生带角度的标签

'''

import numpy,datetime
import matplotlib.pyplot as plot
import matplotlib.ticker as ticker
import matplotlib.dates as dates

start_date = datetime.datetime(2018,3,15)

def make_label(value,pos):
    time = start_date + datetime.timedelta(days = 365 * value)
    return time.strftime('%b %y') # 年：2位， 月缩写

ax = plot.axes()
ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_label))

X = numpy.linspace(0,1,256)
plot.plot(X, numpy.exp(-10 * X),c='r')
plot.plot(X,numpy.exp(-5 * X),c='b',ls='--')


labels = ax.get_xticklabels()
plot.setp(labels,rotation=30.0)
plot.show()