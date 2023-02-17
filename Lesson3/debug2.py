import numpy as np
# this is broken someplace

a = np.arange(15).reshape(3, 5)
attributes_of_a = [
a.shape,
a.ndim,
a.dtype.name,
a.itemsize,
a.size,
type(a),
]

# print out each attribute
for att in attributes_of_a:
        print(att)

b = np.array([6, 7, 8])

# print out the type
print(type(b))