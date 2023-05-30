lst =[12,3,5,7,34,32,65,48,92]

def count(lst):
    
    even=0
    odd=0
    
    for x in range(len(lst)):
        if x%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
even, odd = count(lst)
print(even)
print(odd)