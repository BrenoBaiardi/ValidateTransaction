import re

def returnBitValue(line):
    line = line.split()
    for i in range(len(line)):
        if ":" in line[i]:
            return line[i+1]


s = open('C:/Users/breno.oliveira/Desktop/CT095.txt',mode = "r",encoding="utf8").read()
s = s.split("\n")
for i in range(len(s)):
    if re.search(r'cpo[0-9][0-9][0-9]:', s[i]) or re.search(r'bit[0-9][0-9][0-9]:', s[i]):                      
        #print('found in line'+str(i)+" position "+str(s[i].find(":")-3))
        #print(s[i][s[i].find(":")-3:s[i].find(":")])
        print(returnBitValue(s[i]))
    else:
        continue



'''
def reTest():
    s = '14140445 TRACE 8901   PREV1400   0000    isoproc-cpo012: 191404     '
    match = re.search(r'cpo[0-9][0-9][0-9]:', s)

    if match:                      
        print ('found'), match.group()
    else:
        print ('did not find')

def reFindAll():
    import re
    s = open('C:/Users/breno.oliveira/Desktop/CT095.txt',mode = "r",encoding="utf8").read()
    #s = s.split("\n") #Se for usar o findall deve ser uma única string
    res = re.findall(r'cpo[0-9][0-9][0-9]:', s) 
    for i in res:
        print(i)
'''
