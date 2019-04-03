#!/usr/bin/python3
import sys
from perm import *
import time

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
