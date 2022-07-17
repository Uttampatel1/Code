import numpy as np
import matplotlib.pyplot as plt

xvals = np.arange(-2,1,0.01)

yvals = np.sin(xvals)

plt.plot(xvals, yvals)

plt.show()