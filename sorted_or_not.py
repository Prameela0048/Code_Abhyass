#ascending order
'''def arraySortedOrNot(arr):
    n = len(arr)
    if n == 1 or n == 0:
        return True
    return arr[0] <= arr[1] and arraySortedOrNot(arr[1:])
 
 
arr = [1,2,3,4,5,1,6]

if arraySortedOrNot(arr):
    print("Yes")
else:
    print("No")'''

#descending order
def arraySortedOrNot(arr):
    n = len(arr)
    if n == 1 or n == 0:
        return True
    return arr[0] >= arr[1] and arraySortedOrNot(arr[1:])
 
 
arr = [10,9,8,7,6,5]

if arraySortedOrNot(arr):
    print("Yes")
else:
    print("No")
        
        
