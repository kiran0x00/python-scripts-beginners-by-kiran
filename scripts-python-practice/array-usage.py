from array import *

values=array("i",[])
al=int(input("Enter the length of the array : "))
for x in range(al):
 values.append(int(input("enter value to array : ")))
print(values)

ele_search = int(input("Enter the value for which you need index : "))

k=0
for e in values:
    if e == ele_search:
       print(k)
       break
    k+=1
print(values.index(ele_search))