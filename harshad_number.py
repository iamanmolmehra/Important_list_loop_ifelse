def is_harshad_number(p) :
    sum1=0
    for i in str(p):
        sum1+=int(i)
    b =int(p)//sum1
    print(b)

a=input()
# x_digits = list(str(x)) 
is_harshad_number(a)
