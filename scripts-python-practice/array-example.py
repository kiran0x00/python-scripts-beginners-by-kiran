from array import *

values=array("i",[1,2,3,4,5,6,7,8,9,10])
values.reverse()
for x in range(len(values)):
    print(values[x])
print(values)
print(values.buffer_info())