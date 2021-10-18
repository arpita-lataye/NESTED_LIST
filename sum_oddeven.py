elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=[]
odd=[]
while i<len(elements):
    if elements[i] in elements:
        if elements[i]%2==0:
            even.append(elements[i])
        else:
            odd.append(elements[i])
        i=i+1
print('even list',even)
print('odd list ',odd)
i=0
sumeven=0
average_even=0
while i<len(even):
    sumeven=sumeven+even[i]
    i=i+1
    average_even=sumeven/len(even)
print('sum of even',sumeven)
print('average of sum of even numbers:',average_even)
i=0
sumodd=0
average_odd=0
while i<len(odd):
    sumodd=sumodd+odd[i]
    i=i+1
    average_odd=sumodd/len(odd)
print('sum of odd',sumodd)
print('average of sum of odd numbers:',average_odd)