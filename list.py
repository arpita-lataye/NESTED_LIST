# d=[[2,3,4],[5,7,6]]
# a=[]
# c=[]
# i=0
# while i<len(d):
#     if d[0]not in a:
#         a.append(d[0])
#     i=1
#     while i<len(d):
#         if d[1]not in c:
#             c.append(d[1])
#         i=i+1
#     # i=i+1
# print(a)
# print(c)                            


a=['tina','saloni','panwar','karuna','vishkarma',"sytuioytrgdsfhjkjhg"]
i=0
while i<len(a):
    j=0
    count=0
    max=a[i]
    while j<len(a[i]):
        count=count+1
        if a[i]>max:
          max=a[i]
        j=j+1
    print(count,a[i])
    i=i+1
print('maximum is',count,max)
# print(count,a[i])
# print(max)


# a=[1,2,5,6,[7,8,10]]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i]) is list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j=j+1
#     else:
#         b.append(a[i]) 
#     i=i+1
# print(b)     
# 
# a=[1,2,5,6,[7,8,10]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i]) is list:
#         j=0
#         while j<len(a[i]):
#           sum=sum+a[i][j]
#           j=j+1
#     else:
#           sum=sum+a[i]
#     i=i+1
# print(sum)      