mini=999
second_mini=999
a=[1,1,2,3,4,5]
for i in a:
    if i<mini:
        second_mini=mini
        mini=i
    if i<second_mini and i!=mini:
        second_mini=i
print("second minimum",second_mini)
print("Minimum element",mini)
