pos=-1
lst =[10,2,3,4,6,18,34]
n=1
def search(lst,n):
    l=0
    u=len(lst) -1
    while l <= u:
        mid = (l+u)//2
        if lst[mid]==n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid]<n:
                l=mid
            else:
                u=mid
                     
result=search(lst,n)
if result:
    print("Found in list")
else:
    print("Not found in list")