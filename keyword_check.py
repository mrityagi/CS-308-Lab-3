import re

def keyword_check(ans,path_file1,path_file2):
    """
    A method to find the lines containing specified keywords.

    ans: a variable to store lines containing specified keywords.
    path_file1: path of file where keywords are to be searched from.
    path_file2: path of file containing required keywords.
    """
    file1=open(path_file1,"r")
    file2=open(path_file2,"r")#opening files
    include_words = set() #set of all keywords
    i = 0
    for line in file2: 
        res = re.findall(r'\w+',line)
        for i in res:
            a = i.lower()
            include_words.add(a)        
    for line in file1: 
        for line1 in line.split('.'):
            if(line1=='\n'):
                continue
            res = re.findall(r'\w+',line1) #all words in a line
            for i in res:
                a = i.lower()
                if a in include_words:
                    ans.append(line1)
                    break # if any word is found in include words then no need to iterate furthur
