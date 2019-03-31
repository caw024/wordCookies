#!/usr/bin/python3
import sys
  
def perm(word):
  word = list(word)
  
  

def Process(infile,outfile):
  #f has pair of words to apply wordladder to
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
    curr = word[i]
    length = len(curr)
  
    #get all words of same length
    if length not in mywordlist:
      mywordlist[length] = {}
      for k in wordlist:
        if len(k) == length:
          set = mywordlist[length]
          mywordlist[length] = set.add(k)
          #print(k)

    perms = perm(curr)
    
    
  towrite = '\n'.join(towrite)
  #g is what we will return
  g = open(outfile,'w')
  g.write(towrite)
  g.close()

            
#$ ./fred.py A.txt(words of same length) B.txt
def main():
  Process(sys.argv[1],sys.argv[2])

main()
