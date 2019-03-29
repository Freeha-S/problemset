# modified by:@ Freha
# source : https://matplotlib.org/gallery/pyplots/pyplot_three.html#sphx-glr-gallery-pyplots-pyplot-three-py
import numpy as np
import matplotlib.pyplot as plt

 # evenly sampled x value 0 to 4 at intervals 1
x = np.arange(0, 5, 1)
 # red dashes, blue dashes and green dashes
plt.plot(x, x, 'r--', x, x**2, 'b--', x, 2**x, 'g--')
plt.show()
        