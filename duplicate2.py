# it will be show the numbers how many which time repeat.
# how many number repeat in a list.
n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
a=[]
b=[]
i=0
while i<len(n):
    if n[i]in n:
        if n[i] not in a:
            a.append(n[i])
        else:
            b.append(n[i])
    i=i+1
print(b,'b list')
print(a,'a list')