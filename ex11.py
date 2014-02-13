import re
from sys import argv

script, filename = argv

def egrep (pattern,filename):
    matchlines=[]
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        match = pattern.match(line)
        if match:
            matchline = match.group()
            matchlines.append(matchline)
         
    return len(matchlines)
    





pattern1 = re.compile("[aA]+.*")
print egrep(pattern1, filename) 
