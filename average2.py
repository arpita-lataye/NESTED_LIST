marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
i=0
while i<len(marks):
    if len(marks)>0:
        j=0
        sum=0
        average=0
        while j<len(marks[i]):
            sum=sum+(marks[i][j])
            j=j+1
            average=sum/len(marks[i])
        i=i+1
        print('sum',sum)
        print('average of',i,'year',average)