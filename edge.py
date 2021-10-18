marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
]
i=0
m=len(marks)
sum=0
while i<m:
    if len(marks[i])>0:
        j=0
        b=len(marks[i])
        while j<b:
            sum=sum+marks[i][j]
            j=j+1
        i=i+1
print(sum)
