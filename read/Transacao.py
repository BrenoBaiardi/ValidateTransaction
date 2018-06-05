import re

class Transacao:
    'Classe que diz respeito ao arquivo de transação e suas linhas de dados'

    def __init__(self, filepath, NSU):
        self.filepath = filepath
        self._NSU = NSU
        self._file = open(self.filepath , mode = "r" , encoding="utf8")
        self._lines = self._file.read()
        self._file.close()
        
    def _getBitValue(self, line):
        line = line.split()
        for i in range(len(line)):
            if ":" in line[i]:
                return line[i+1]
            
    def getNSU(self):
        return self._NSU

    def getFilepath(self):
        return self.filepath

    def parseFile(self):
        s = self._lines.split("\n")
        data =[]
        aux=[]
        for i in range(len(s)):
            if re.search(r'NSU:', s[i]) and str(self._NSU) in s[i]:
                if len(aux) > 0:
                    data.append(aux)    
                aux=[]
            if re.search(r'cpo[0-9][0-9][0-9]:', s[i]) or re.search(r'bit[0-9][0-9][0-9]:', s[i]):                      
                aux.append("Bit" + s[i][s[i].find(":")-3:s[i].find(":")] + "->" + self._getBitValue(s[i]))
                #print("bit ->" + s[i][s[i].find(":")-3:s[i].find(":")])
                #print("valor ->" + self.__getBitValue(s[i]))
            else:
                continue

        if len(aux) > 0: #atribuição da ultima ponte, não atribuida por não encontrar outro início
            data.append(aux)    
        return data
    
    def readBits(self):
        s = self._lines.split("\n")
        for i in range(len(s)):
            if re.search(r'cpo[0-9][0-9][0-9]:', s[i]) or re.search(r'bit[0-9][0-9][0-9]:', s[i]):                      
                #print('found in line'+str(i)+" position "+str(s[i].find(":")-3))
                print("bit ->" + s[i][s[i].find(":")-3:s[i].find(":")])
                print("valor ->" + self.__getBitValue(s[i]))
            else:
                continue

    def readBit(self,bit):
        bit = str(bit)
        while len(bit) < 3:
            bit = "0" + bit
        s = self._lines.split("\n")
        for i in range(len(s)):
            if re.search(r'cpo[0-9][0-9][0-9]:', s[i]) or re.search(r'bit[0-9][0-9][0-9]:', s[i]):                      
                if s[i][s[i].find(":")-3:s[i].find(":")] == bit:
                    print("bit ->" + s[i][s[i].find(":")-3:s[i].find(":")])
                    print("valor ->" + self.__getBitValue(s[i]))
            else:
                continue

    def _findBitInList(self,bit,bit_list):
        bit = str(bit)
        while len(bit) < 3:
            bit = "0" + bit
        for i in bit_list:
            if bit in i[:6]:
                return i
        return 0

    def compareBits(self):
        data = self.parseFile()
        print(data[0]==data[1])
        for i in range(1,128):
            for c in range(len(data)):
                print("perna" + str(c+1), end="\t")
                if self._findBitInList(i,data[c]):
                    print(self._findBitInList(i,data[c]))
                else:
                    print("Bit" + "%03d" % i+" Não encontrado")
                    #print("{0:0=2d}".format(i))
            print("") #separador de bits por linha
        
    
#NSU:945037
tran = Transacao('C:/Users/breno.oliveira/Desktop/CT095.txt', NSU = 945037)
