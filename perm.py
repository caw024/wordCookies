#unique elements, generate all arrangements of n numbers

def perm(data):
    data = list(data)
    usednums = []
    #unusednums is a dict
    unusednums = {}
    #total perm is a set
    totalperm = {0}
    totalperm.remove(0)
    for i in data:
        if i in unusednums:
            unusednums[i] += 1
        else:
            unusednums[i] = 1

    return poss(unusednums,usednums,totalperm)
    
    #you have all the #s, now find their arragements
    #return poss(unusednums,usednums,totalperm,currwordlist)


def newdict(available):
  mydict = {}
  for k in available:
    mydict[k] = available[k]
  return mydict

def poss(unusednums,usednums,totalperm):
    if len(unusednums) == 0:
        #newstr = "".join(usednums[:] + unusednums)
        newstr = "".join(usednums[:])
        totalperm.add(newstr)
        return totalperm
    else:
        nullset = {0}
        nullset.remove(0)
        semiperm = nullset.union(totalperm)
        for k in unusednums:
            currunused = newdict(unusednums)
            currused = usednums[:]
            currperm = nullset.union(semiperm)
            #currstring = "".join(list(string)) + k

            currunused[k] -= 1
            if currunused[k] == 0:
                del currunused[k]
            totalperm = totalperm.union( poss(currunused,currused,currperm) )

            currused.append(k)
            totalperm = totalperm.union( poss(currunused,currused,currperm) )
            #print(k,currperm,currunused,currused)
            #print(semiperm,unusednums,usednums)
        return totalperm


#print( perm("abcd") )
#print( perm("carthors") )

