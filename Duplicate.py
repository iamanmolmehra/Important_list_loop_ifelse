# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
d=[]
# for i in n:
#     if i not in d:
#         d.append(i)
# print(d)

[d.append(i) for i in [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] if i not in d ]
print(d)





