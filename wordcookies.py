#!/usr/bin/python3
import sys
from perm import *  
  

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
  while i < len(words):
    curr = words[i]
    length = len(curr)
  
    #get all words into dict with key = length, val = set of possibilities
    if length not in mywordlist:
      mywordlist[length] = {0}
      for k in wordlist:
        if len(k) == length:
          myset = mywordlist[length]
          myset.add(k)
          mywordlist[length] = myset
          #print(k)

    currwordlist = mywordlist[length]

    allperms = perm(curr)
    print("allperms: ")
    print(allperms)
    pushstr = curr + ":"
    for k in allperms:
      if k in currwordlist:
        if k != curr:
          pushstr += k + ","
    pushstr = pushstr[:-1]
    towrite.append(pushstr)

    i+=1
  print("towrite: ")
  print(towrite)
  towrite = '\n'.join(towrite)
  #g is what we will return to harry.txt
  g = open(outfile,'w')
  g.write(towrite)
  g.close()

            
#$ ./fred.py A.txt(words of same length) B.txt
def main():
  Process(sys.argv[1],sys.argv[2])

main()
