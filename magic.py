
magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]]

i=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square[i]):
        sum=sum+magic_square[i][j]
        j=j+1
    print(i,'row',sum)

    j=0
    sum1=0
    while j<len(magic_square):
        sum1=sum1+magic_square[j][i]
        j=j+1
    print(i,'column',sum)
    i=i+1
print()
g=0
sum2=0
while g<len(magic_square):
    sum2=sum2+magic_square[g][g]
    g=g+1
print('diagonal1',sum2)
print()
k=0
sum3=0
while k<len(magic_square):
    p=(len(magic_square)-1)-k
    while p<(len(magic_square)-k):
        sum3=sum3+magic_square[k][p]
        p=p+1
    k=k+1
print('diagonal2',sum3)
print()
if sum==sum1==sum2==sum3:
    print('this is a magic sqaure')
else:
    print('this is not a magic square')