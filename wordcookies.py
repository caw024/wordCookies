#!/usr/bin/python3
import sys
from perm import *
import time
def Process(infile,outfile):
  #f has the words in fred.txt
  f = open(infile, 'r')
  words = f.read().split('\n')
  f.close()


  #word list
  dictall = open('dictall.txt','r')
  wordlist = dictall.read().split('\n')
  dictall.close()

  mywordlist = {}
  towrite = []
  checked = {}

  i = 0
  while i < len(words) and len(words[i]) > 0:
    curr = words[i]
    length = len(curr)

    #get all words into dict with key = length, val = set of possibilities
    while length > 0:
      if length not in mywordlist:
        mywordlist[length] = {0}
        for k in wordlist:
          if len(k) == length:
            myset = mywordlist[length]
            myset.add(k)
            mywordlist[length] = myset
            #print(k)
      length-=1

    start = time.time()
    allperms = perm(curr)
    total = time.time()-start
    
    pushstr = curr + ": " + str(total)
    pushdict = {}
    for k in allperms:
      templen = len(k)
      if templen > 0 and k in mywordlist[templen]:
        if k != curr:
          if templen not in pushdict:
            pushdict[templen] = {k}
          else:
            myset = pushdict[templen]
            myset.add(k)
            pushdict[templen] = myset
    max = 0
    for j in pushdict:
      if max < j:
        max = j

    ctr = 0
    while ctr <= max:
      if ctr in pushdict:      
        pushstr += "\n\tlength " + str(ctr) + ": " + str(len(pushdict[ctr])) + "\n\t\t"
        for a in pushdict[ctr]:
          pushstr += a + ","
        pushstr = pushstr[:-1]
      ctr += 1
    towrite.append(pushstr)

    i+=1
  towrite = '\n'.join(towrite)
  #g is what we will return to harry.txt
  g = open(outfile,'w')
  g.write(towrite)
  g.close()

def Process2(inputfile,outputfile):
    #f has the words in fred.txt
    f = open(inputfile, 'r')
    g = open(outputfile,'w')
    #word list
    dictall = open('dictall.txt','r')
    for line in f:
        res = []
        line = line.strip()
        letterbucket = {}
        for i in line:
            if i in letterbucket.keys():
                letterbucket[i] += 1
            else:
                letterbucket[i] = 1
        for word in dictall:
          word = word.strip()
          add = True
          d = letterbucket.copy()
          if len(word) <= len(d.keys()):
            for l in word:
              if l in d.keys():
                if d[l] == 0:
                  add =False
                  break
                else:
                  d[l] -= 1
              else:
                add = False
                break
            if add:
              res.append(word)
            ans = ','.join(res)
            g.write(ans)
    f.close()
    g.close()
    dictall.close()



#$ ./fred.py A.txt(words of same length) B.txt
def main():
  Process2(sys.argv[1],sys.argv[2])

start = time.time()
main()
end = time.time()
print(end - start)
