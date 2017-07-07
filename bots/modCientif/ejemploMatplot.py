###################
# Modulo matplotlib
###################

import matplotlib.pyplot as plt
import numpy as np

"""plt.plot([1,2,3,4])

plt.ylabel("Eje y")
plt.xlabel("Eje x")

plt.show()"""

x=np.linspace(-15,15,200)
y=np.sin(x)/x

plt.plot(x,y)
plt.plot(x,y,'co')
plt.plot(x,2*y,x,3*y)


plt.show()