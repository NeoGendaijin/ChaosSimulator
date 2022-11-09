import numpy as np
import scipy.ndimage.filters
import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 20,10
lap = lambda X: scipy.ndimage.filters.laplace(X)

I = 0.325 # external input
c = 10 # 10
a = 0.5 #0.7
b = 0.8 #0.8
'''
Du=0.5, Dv=1 repeating
'''
def update(U, V, Du=0.3, Dv=0.6): # Du=0.2, Dv=1.8
    return (Du*lap(U) + c * (-V + U - pow(U,3)/3 + I),
            Dv*lap(V) + U - b * V + a)

size = (128*3, 128*3)
U = np.random.random(size)
V = np.random.random(size)
dt = 0.1

fig = plt.figure()
ax = fig.add_subplot(111)
img = ax.imshow(U, interpolation="nearest", cmap=plt.cm.gray)

view_interval = 10
for i in range(10000):
    dU, dV = update(U, V)
    U += dt*dU
    V += dt*dV
    if i % view_interval == 0:
        img.set_data(U)
        
        ax.set_title("t = {}".format(i))
        plt.pause(0.1) #0.1
plt.show()
