n = list(input("Enter some alphabets : "))
a=[]
for i in n :
    b = n.count(i)
    d=[i,b]
    if d not in a:
        a.append(d)
    
print(a)
           