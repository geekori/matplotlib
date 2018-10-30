# 定制曲线的类型

import numpy
import matplotlib.pyplot as plt
X = numpy.linspace(-6,6,1024)
plt.plot(X, -X**2,color='r',linestyle='solid')
plt.plot(X, -X**2 + 3, color='b',linestyle='dashed')
plt.plot(X,-X**2 + 6,color='k',linestyle='dashdot')
plt.show()