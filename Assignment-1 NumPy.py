# Q-1 Create a null vector of size 10 but the fifth value which is 1.

import numpy as np
x = np.zeros(10)
print(x)
print("Update fifth value to 1")
x[4] = 1
print(x)

# Q-2 Create a vector with values ranging from 10 to 49

import numpy as np
v = np.arange(10,50)
print("Original vector:")
print(v)

# Q-3 Create a 3x3 matrix with values ranging from 0 to 8

import numpy as np
a =  np.arange(9).reshape(3,3)
print(a)

# Q-4 Find indices of non-zero elements from [1,2,0,0,4,0]

import numpy as np
nz = np.nonzero([1,2,0,0,4,0])
print(nz)

# Q-5  Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np
x = np.random.random((10,10))
print("Original Array:")
print(x) 
xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax) 

# Q-6 reate a random vector of size 30 and find the mean value.

import numpy as np
Z = np.random.random(30)
m = Z.mean()
print (m)