'''
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
plt.show()

'''
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100)
#print(np.average(data))
print(data)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (8, 4))
print(fig)


ax1.hist(data,20)
ax2.boxplot(data)

plt.show()