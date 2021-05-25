a = int(input('Enter a number : \n'))
b = int(input('Enter a number : \n'))
c = int(input('Enter a number : \n'))

if a==b and b==c :
    print ('They all are equal')
elif b>=a and b>=c :
    print(b, "is greater")
elif c>=b and c>=a :
    print(c, "is greater")   
elif a>=b and a>=c :
    print(a, " is greater")



