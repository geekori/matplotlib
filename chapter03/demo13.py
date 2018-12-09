'''

绘制多边形

Polygon(points,color,...,)
'''

import numpy
import matplotlib.pyplot as plot

values = numpy.linspace(0,2*numpy.pi, 8)
print(values)
points = numpy.vstack((numpy.cos(values),numpy.sin(values))).transpose()
print(points)
plot.gca().add_patch(plot.Polygon(points,lw=10,edgecolor='b',facecolor='r'))
plot.grid(True)
plot.axis('scaled')
plot.show()
