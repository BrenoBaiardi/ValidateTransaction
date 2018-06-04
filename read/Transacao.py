import re


class Transacao:
    'Classe que diz respeito ao arquivo de transação e suas linhas de dados'
    linhas = []

    def __init__(self, filepath, NSU):
        self.filepath = filepath
        self.NSU = NSU
        self.file = open(self.filepath , mode = "r" , encoding="utf8") 

    def getBitValue(self, line):
        line = line.split()
        for i in range(len(line)):
            if ":" in line[i]:
                return line[i+1]
            
    def getNSU(self):
        return self.NSU

    def getFilepath(self):
        return self.filepath

    def read(self):
        s = self.file.read().split("\n")
        for i in range(len(s)):
            if re.search(r'cpo[0-9][0-9][0-9]:', s[i]) or re.search(r'bit[0-9][0-9][0-9]:', s[i]):                      
                #print('found in line'+str(i)+" position "+str(s[i].find(":")-3))
                #print(s[i][s[i].find(":")-3:s[i].find(":")])
                print(self.getBitValue(s[i]))
            else:
                continue

    
