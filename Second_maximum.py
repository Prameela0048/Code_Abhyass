#1)find the second largest and second smallest element in the array
#2)remove duplicates from the array
#3)right rotate the array by one position

maxi=-9999
second_maxi=-999
a=[100,100,2,3,4,5,5,5,100,100]
for i in a:
    if i>maxi:
        second_maxi=maxi
        maxi=i
    if i>second_maxi and i!=maxi:
        second_maxi=i
print("second maximum",second_maxi)
print("Maximum element",maxi)
        
    
