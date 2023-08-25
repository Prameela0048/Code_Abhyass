#binary search


def search(a,target):
    n=len(a)
    low=0
    high=n-1
   
    while low<=high:
        mid=low+(high-low)//2
        if a[mid]==target:
            return mid
            break
        elif a[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

a=[1,3,4,5,6,7,8]
target=100
res=search(a,target)

print(res)

#linear search

def li_search(arr,target):
    n=len(a)
    for i in range(n):
        if a[i]==target:
            return i
    return -1
target=100
result=search(a,target)
print(result)

