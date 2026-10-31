import numpy as np
x = np.array([1, 0])
w = np.array([0.5, 0.4])
print("Output:", int(np.dot(x, w) >= 0.5))
