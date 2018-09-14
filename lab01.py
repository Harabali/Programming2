import numpy as np
import math
#EX1:
l = np.random.randint(0,100,30)
setA = set(l)

minV = np.inf
maxV = -np.inf
for i in setA:
    if i > maxV:
        maxV = i

    if i<minV:
        minV = i

print(setA)
print('The minimum value in setA: {}'.format(minV))
print('The maximum values in SetA:', maxV)


#EX2:
str = '*'
N = 16
for i in range(1,N+1):
    if i<=math.ceil(float(N)/2):
        print(i*str)
    else:
        print((N+1-i)*str)



#EX3:
r = int(input('Give me the number of rows:'))
c = int(input('Give me the number of colums:'))
M = np.zeros((r,c))
for i in range(0,r):
    for j in range(0,c):
        M[i,j] = i*j

print(M)
