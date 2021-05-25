magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 

d1 = 0
d2 = 0
d1 = d1+ magic_square[0][0] + magic_square[1][1] + magic_square[2][2] 
d2 = d2 + magic_square[2][0] + magic_square[1][1] + magic_square[0][2]
print (d1, d2, end = ' ')

temp = 0
sum = 0
num = 0
for i in magic_square :
    temp = temp + i[0]
    num = num + i[1]
    sum = sum + i[2]

for p in magic_square :
    ram=0
    for k in p :
        ram = ram + k 
    print (ram, end = ' ')
print(temp,num,sum)



