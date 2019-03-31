#unique elements, generate all arrangements of n numbers

def perm(data):
    possible = []
    numbers = []
    total = []
    for i in data:
        numbers.append(i)
    num = len(numbers)
    fact = 1
    for k in range(1,num+1):
        fact *= k
    
    #you have all the #s, now find their arragements
    return poss(possible,numbers,total,fact)

#current list, remaining numbers
def poss(list,remnum,fin,fact):
    if len(fin) == fact:
        return fin
    if remnum == []:
        fin.append(list)
        return
    else:
        i = len(remnum)-1
        while (i >= 0):
            a = []
            b = []
            for j in remnum:
                a.append(j)
            for k in list:
                b.append(k)
            val = a[i]
            del a[i]
            b.append(val)
            return poss(b,a,fin,fact)
            i-=1
        

perm([1,2,3])
        
    
    
#know how to write to files
#how to classes + working w priority queue in heap form
