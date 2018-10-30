# 使用LaTeX格式的标题

# 是一种基于TEX的排版系统

import numpy
import matplotlib.pyplot as plt

X = numpy.linspace(-4,4,1024)
Y = .25 * (X + 4) * (X + 1) * (X - 2)
plt.title(r'$f(x) = \frac{1}{4}(x+4)(x+1)(x-2)$')
plt.plot(X,Y, c='b')
plt.show()
