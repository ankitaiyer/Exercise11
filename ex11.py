import re
from sys import argv

script, filename = argv

# Matches the pattern in the given file and returns the count# it matched
def egrep (pattern,filename):
    matchlines=[]
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        match = pattern.search(line)
        if match:
            matchline = match.group()
            matchlines.append(matchline)
         
    return len(matchlines)
    


#All the words that begin with the letter a, independent of case (17096 words)
pattern1 = re.compile("^[aA]+.*")
print "Words expected-17096, words actual", egrep(pattern1, filename)

pattern2 = re.compile("ing")
print "Words expected-8852, words actual", egrep(pattern2, filename)

pattern3 = re.compile("ing$")
print "Words expected-5539, words actual", egrep(pattern3, filename)

pattern4 = re.compile("^\w{7}$")
print "Words expected-23869, words actual", egrep(pattern4, filename)

pattern5 = re.compile("\w*aa\w*")
print "Words expected-124, words actual", egrep(pattern5, filename)

pattern6 = re.compile("\w*(vark|wolf)$")
print "Words expected-8, words actual", egrep(pattern6, filename)