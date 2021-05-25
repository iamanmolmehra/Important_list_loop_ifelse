sum_list=[]
n = [10, 11, 12, 13, 14, 17, 18, 19] 

for i in n :
    for j in n:
        if i+j==30:
            sum_list.append([i,j])
            sum_list.insert(len(sum_list), [i,j])
print(sum_list)

            
