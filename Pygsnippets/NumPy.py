import numpy as np

a = np.array([1.0, 2.0, 3.0, 4.0])
b = np.array([4.0, 3.0, 2.0, 1.0])
for item in a:  # arrays are iterable
    print(item)
c = a + b  # c = [5, 5, 5, 5]
print(a[0:3:2])  # 1.0, 3.0; last element not included!
a[0:3] = b[0:-1]

print(a*b)  # prints [4, 6, 6, 4], not the scalar product!
