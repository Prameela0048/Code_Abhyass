dic={}
a=[3,3,4,4,5,6,6,6,6,8,8,8,8,8,8,8,100]
maxi=0
mini=999
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
min_key=min(dic,key=lambda x:dic[x])
print(min_key)
