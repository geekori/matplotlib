'''
将图表保存未pdf文档

'''

import numpy
import matplotlib.pyplot as plt

X = numpy.linspace(-6,6,1024)
Y= numpy.sinc(X)

plt.figure(figsize=(15,12)) # 15 * 72   12 * 72
plt.plot(X,Y)
plt.savefig('sinc.pdf')

