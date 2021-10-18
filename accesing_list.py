a=[10,20,30,[50,60]]
length=len(a)
i=0
while i<length:
    if type (a[i]) is list:
        if len(a[i])>1:
            j=0
            m=len(a[i])
            while j<m:
                print(i,j,a[i][j])
                j=j+1
            i=i+1
    else:
        print(i,a[i])
        i=i+1
