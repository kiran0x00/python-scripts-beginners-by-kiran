lst =[10,2,3,4,6,18,34]
n=1
def search(lst,n):
    i=0
    while i < len(lst):
        if lst[i] == n:
            return True
        i=i+1
    return False
result=search(lst,n)
if result:
    print("Found in list")
else:
    print("Not found in list")