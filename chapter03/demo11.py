'''

在坐标系上绘制多条彩色线条

Line2D((X1,X2),(Y1,Y2),color=...)

'''

import matplotlib.pyplot as plot

N = 16

colors = ['r','b','y','0.5','g']

for i in range(N):
    # (0,0), (16,0)
    # (0,1), (15,0)
    plot.gca().add_line(plot.Line2D((0,i),(N-i,0),color=colors[i % len(colors)]))

plot.gca().add_line(plot.Line2D((0,20),(13,13),color='r'))
plot.grid(True)
plot.axis('scaled')
plot.show()
