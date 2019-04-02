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

            
#$ ./fred.py A.txt(words of same length) B.txt
def main():
  Process(sys.argv[1],sys.argv[2])

main()
