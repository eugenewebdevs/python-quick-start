# We can import a package and give a shorter name.
# plt is an example

import matplotlib.pyplot as plt
import numpy as np

# now we can access (and chain) functions in the library via dot notation
# Below we employ the library functions style and use()
plt.style.use('_mpl-gallery-nogrid')

# make data: correlated + noise
np.random.seed(1)
x = np.random.randn(5000)
y = 1.2 * x + np.random.randn(5000) / 3

# plot:
fig, ax = plt.subplots()

ax.hexbin(x, y, gridsize=20)

ax.set(xlim=(-2, 2), ylim=(-3, 3))

# let's see what we get
plt.show()
