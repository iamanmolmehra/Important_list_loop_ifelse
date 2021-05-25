a = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]] 
 
o = [] 
  
def nest(a): 
    for i in a: 
        if type(i) == list: 
            nest(i) 
        else: 
            o.append(i) 
   
print ('The original list: ', a) 
nest(a) 
print ('The list after removing nesting: ', o) 