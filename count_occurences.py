char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
s=[]
while i<len(char_list):
    j=0
    n=[]
    count=0
    while j<len(char_list):
        if char_list[i] in char_list:
            if char_list[i]==char_list[j]:
                count=count+1
        j=j+1
    n.append(char_list[i])
    n.append(count)
    if n not in s:
        s.append(n)
    i=i+1
print(s)
