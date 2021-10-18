a=[1,2,3,4,5,6]
b=[0,2,1,3,7,8]
c=[]
i=0
while i<len(a):
    if a[i] not in b:
        c.append(a[i])
        # print(c)
    i=i+1
print(c)