import numpy as np
import matplotlib.pyplot as plt

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print("Vector A:", A)
print("Vector B:", B)
print("Vector Addition:", A + B)
print("Vector Subtraction:", A - B)
print("Dot Product:", np.dot(A, B))

M1 = np.array([[1, 2], [3, 4]])
M2 = np.array([[5, 6], [7, 8]])

print("Matrix Addition:\n", M1 + M2)
print("Matrix Multiplication:\n", np.dot(M1, M2))
print("Transpose:\n", M1.T)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(A, marker='o', label="Vector A")
plt.plot(B, marker='s', label="Vector B")
plt.title("Vector Operations")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.imshow(M1, cmap="viridis")
plt.colorbar()
plt.title("Matrix Visualization")
plt.xlabel("Column")
plt.ylabel("Row")

plt.tight_layout()
plt.show()
