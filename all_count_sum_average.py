elements=[32,41,65,21,91,9,51,52,31,24,34]
i=0
count=0
count_even=0
count_odd=0
even=[]
odd=[]
sum=0
sum_even=0
sum_odd=0
average_even=0
average_odd=0
average=0
while i<len(elements):
    if i%2==0:
        even.append(elements[i])
        count_even=count_even+1
        sum_even=sum_even+elements[i]
        average_even=sum_even/len(even)
    else:
        odd.append(elements[i])
        count_odd=count_odd+1
        sum_odd=sum_odd+elements[i]
        average_odd=sum_odd/len(odd)
    count=count+1
    sum=sum+elements[i]
    average=sum/len(elements)
    i=i+1
print('total of even',count_even)
print('total of odd',count_odd)
print('total elements:',count)
print()
print('even list',even)
print('odd list',odd)
print()
print('sum of even elements:',sum_even)
print('sum of odd elements:',sum_odd)
print('total sum of elements',sum)
print()
print('average of sum of even elements is:',average_even)
print('average of sum of odd elements is:',average_odd)
print('average of total sum of elements is:',average)
