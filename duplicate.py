# h=[2,3,4,5,3,6,5, 4,3]
# g=[]
# i=0
# while i<len(h):
#     j=0
#     count=0
#     while j<len(h):
#         if h[i]==h[j]:
#            count=count+1
#            if count>=2:
#               if h[i] not in g:
#                   g.append(h[i])
#         j=j+1
#     i=i+1
# print(g)


# it will be show which number repeat in a list.
n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
a=[]
i=0
while i<len(n):
    j=0
    count=0
    while j<len(n):
        if n[i]==n[i]:
            count=count+1
            if count>=2:
                if n[i]not in a:
                    a.append(n[i])
        j=j+1
    i=i+1
print(a)
