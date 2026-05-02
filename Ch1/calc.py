import numpy as np

print("Four Arithmetic Operations")
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x/2.0)

A = np.array([[1.0, 2.0],
              [3.0, 4.0]])
B = np.array([[3.0, 0.0],
              [0.0, 6.0]])

print(A + B)
print(A * B)

# Broadcast
print("\nBroadcast")
A = np.array([[1.0, 2.0],
              [3.0, 4.0]])

B = np.array([10, 20])

print(A + B)
print(A * B)

# Matrix Operations
print("\nMatrix Operations")

A = np.array([[51, 55],
              [14, 19],
              [0, 4]])

print(A[0])
print(A[0][1])

for row in A:
    print(row)

A = A.flatten()

print(A)
print(A[np.array([0, 2, 4])])
print(A > 15)
print(A[A > 15])