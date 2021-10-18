
a = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
d=len(a)
i=0
sum=0
while i<d:
    if len(a[i])>0:
        j=0
        f=len(a[i])
        while j<f:
            sum=sum+a[i][j]
            j=j+1
        i=i+1
    print('total sum of a is:',sum)

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]
# i=0
# m=len(marks)
# sum=0
# while i<m:
#     if len(marks[i])>0:
#         j=0
#         f=len(marks[i])
#         while i<f:
#             sum=sum+marks[i][j]
#             j=j+1
#         i=i+1
# print(sum)

