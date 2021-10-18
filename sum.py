number=30
n=[10, 11, 12, 13, 14, 17, 18, 19]
i=0
while i<len(n):
    j=0
    sum=0
    while j<len(n):
        sum=n[i]+n[j]
        if sum==number:
            print([n[i],n[j]],end='')
        j=j+1
    i=i+1