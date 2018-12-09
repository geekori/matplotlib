'''

绘制不同形态的图形



'''

import matplotlib.patches as patches
import matplotlib.pyplot as plot

# Circle
shape = patches.Circle((0,0),radius = 1,color='red')
plot.gca().add_patch(shape)

# Rectangle
shape = patches.Rectangle((2.5,-0.5),2.0,1,color='blue')
plot.gca().add_patch(shape)

# Ellipse
shape = patches.Ellipse((0,-2.0),2.0,1.0,angle=67,color='yellow')
plot.gca().add_patch(shape)

# Fancy box
#shape = patches.FancyBboxPatch((2.5,-2.5),2.0,1.0,boxstyle='round',color='#FF00FF')
shape = patches.FancyBboxPatch((2.5,-2.5),2.0,1.0,boxstyle='square',color='#FF00FF')
#shape = patches.FancyBboxPatch((2.5,-2.5),2.0,1.0,boxstyle='sawtooth',color='#FF00FF')
plot.gca().add_patch(shape)

plot.grid(True)
plot.axis('scaled')
plot.show()

