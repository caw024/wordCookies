#unique elements, generate all arrangements of n numbers

def perm(data):
    data = list(data)
    usednums = []
    unusednums = []
    totalperm = []
    for i in data:
        unusednums.append(i)
    num = len(unusednums)
    string = ""
    
    #you have all the #s, now find their arragements
    return poss(unusednums,usednums,totalperm,string)


def poss(unusednums,usednums,totalperm,string):
    if unusednums == None:
        totalperm.append(string)
        print(string)
        return totalperm
    else:
        semiperm = totalperm[:]
        for k in unusednums:
            currperm = semiperm[:]
            currunused = unusednums[:]
            currused = usednums[:]
            currstring = "".join(list(string))

            totalperm += poss(currunused.remove(k),currused.append(k),currperm,currstring+k)
        return totalperm
        
                

print( perm(['a','b','c']) )
