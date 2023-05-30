from numpy import *

"""
Type of arrays in num py
1) array()
2) linspace()
3) logspace()
4) arrange()
5) zeros()
6) ones()
"""

# 1) array() it is a normal type of array but works faster than legasy arrays 
arr=array([2,3,4,5,6,7,8,9])
for i in arr:
    print(i)

# 2) linspace() a array with start and end and how many parts we need 
linspace_array=linspace(0,16,15)
print(linspace_array)

# 3) arange() creates array with starting and end and a step range if it is 2 it prents elements with step count 2 Ex: 2,4,6,8,10 ect.
arran=arange(0,16,2)
print(arran)

# 4) zeros() creates array and initializes with zero
array_zero=zeros(5,int)
print(array_zero)

# 5) ones() creates array and initializes with zero
array_ones=ones(5,int)
print(array_ones)

# 6) logspace() a array with start and end and how many parts we need parts split will be based on the log of the value
array_logspace=logspace(0,16,2)
print(array_logspace)  

