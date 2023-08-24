a=[3,3,7,4,5,6,7,3,4,2,7,9,7,0]
n=len(a)
k=2 #no of positions
a=a[n-k:]+a[:n-k]
print(a)
