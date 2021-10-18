
a = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
i=0
l=len(a)
sum=0
while i<l:
    if len(a[i])>1:
        j=0
        m=len(a[i])
        while j<m:
            sum=sum+(a[i][j])
            j=j+1
        i=i+1
    print(sum)

