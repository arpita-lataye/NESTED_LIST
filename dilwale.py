money=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
while i<len(money):
    if money[i]>=10000000:
        print('crorepati')
    elif money[i]>=100000:
        print('lakhpati')
    else:
        print('dilwale')
    i=i+1