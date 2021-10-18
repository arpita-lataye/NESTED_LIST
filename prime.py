a=[20,30,3,7,23,1,9,97,25,5]
i=0
while i<len(a):
    if a[i]%2!=0 and a[i]%3!=0 and a[i]%5!=0:
        print('it is a prime number:',a[i])
    elif a[i]==2 or a[i]==3 or a[i]==5:
        print('it is a prime number:',a[i])
    else:
        print('it is not a prime number:',a[i])
    i=i+1