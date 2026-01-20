import numpy as np

arr = np.arange(1, 16)

print(arr)
print(arr.shape)
print(arr.size)
print(arr.dtype)

arr[0] = 100
arr[-1] = 200
print(arr)

arr2d = np.arange(1, 13).reshape(3, 4)

print(arr2d.shape)
print(arr2d[0, 1])
print(arr2d[1])
print(arr2d[:, 2])

arr3 = np.arange(1, 13)

matrix1 = arr3.reshape(4, 3)
matrix2 = arr3.reshape(2, 6)

flat = matrix1.flatten()
print(flat)

arr4 = np.arange(1, 21)

print(arr4[arr4 > 10])
print(arr4[arr4 % 2 == 0])

arr4[arr4 < 5] = 0
print(arr4)

arr5 = np.array([2, 4, 6, 8, 10])

print(arr5 ** 2)
print(np.sqrt(arr5))
print(np.mean(arr5))
print(np.std(arr5))

arr6 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(np.sum(arr6))
print(np.sum(arr6, axis=1))
print(np.sum(arr6, axis=0))
print(np.mean(arr6, axis=1))

scores = np.array([55, 70, 85, 90, 40, 60])

print(np.sum(scores >= 60))

scores[scores < 60] += 10
print(scores)
