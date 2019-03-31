#unique elements, generate all arrangements of n numbers

def perm(data):
    data = list(data)
    usednums = []
    unusednums = []
    #total perm is a set
    totalperm = {0}
    totalperm.remove(0)
    for i in data:
        unusednums.append(i)

    return poss(unusednums,usednums,totalperm)
    
    #you have all the #s, now find their arragements
    #return poss(unusednums,usednums,totalperm,currwordlist)


def poss(unusednums,usednums,totalperm):
    if len(unusednums) == 1:
        newstr = "".join(usednums[:] + unusednums)
        #if newstr in currwordlist:
        totalperm.add(newstr)
        return totalperm
    else:
        nullset = {0}
        nullset.remove(0)
        semiperm = nullset.union(totalperm)
        for k in unusednums:
            currunused = unusednums[:]
            currused = usednums[:]
            currperm = nullset.union(semiperm)
            #currstring = "".join(list(string)) + k

            currunused.remove(k)
            currused.append(k)
           
            totalperm = totalperm.union( poss(currunused,currused,currperm) )
            #print(k,currperm,currunused,currused)
            #print(semiperm,unusednums,usednums)
        return totalperm
#observations: can handle only 9 distinct letters at a time
#if some repeated letters, the computer may be able to handle it
