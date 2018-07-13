import re
import os

class Log():
    bit_pattern = re.compile(r"(bit|cpo)\d{3}: ")
    # NSU:925325
    # NSU:402383
    # NSU:402386
    # NSU:000275 8 pernas
    # NSU:001742 8 pernas log bagunçado 05 - 07 12:30

    def __init__(self,NSU,log_path):

        self.log_path = log_path
        self.NSU = r"NSU:" + NSU # inserir NSU da transacao
        self.NSU_pattern = re.compile(self.NSU)
        self.matches = []
        self.pernas={}
        self.data=[]

    def __findMatches(self):
        self.matches = []
        for filepath in os.listdir(self.log_path):
            file = open(self.log_path + filepath, mode="r",
                        encoding="utf-8", errors='replace')
            lines = file.readlines()
            file.close()

            for row in lines:
                #input(self.NSU_pattern.search(row))
                if self.NSU_pattern.search(row) != None:
                    self.matches.append(row)
                    print(self.NSU + " - found in file - " + filepath)
                else:
                    continue
            print(self.NSU + " - not found in - " + filepath)


            self.data.extend(lines)
            #self.data = list(set(self.data + lines))

            #self.data.extend(x for x in lines if x not in self.data)

        print("!@#!@#!@#!@#!@#@!#\n")
        print(len(lines))
        print(len(self.data))
        print(len(self.data+lines))
        #for i in self.data:print(i)
        print("\n!@#!@#!@#!@#!@#@!#")
        return self.matches

    def getData(self):
        matches = self.__findMatches()
        if len(matches)!=0:
            for i in range(len(matches)):
                aux={} # cria dict auxiliar
                print('{0:=^100}'.format(''))
                print(matches[i],end='')
                print('{0:=^100}'.format(''))
                start_row = self.data.index(matches[i])
                inner_row = start_row + 2
                while "NSU:" not in self.data[inner_row]:#enquanto não encontrar uma linha contendo outro ou o memso NSU
                    if self.bit_pattern.search(self.data[inner_row]):
                        span = self.bit_pattern.search(self.data[inner_row]).span()
                        aux[self.data[inner_row][span[0]+3:span[0]+6]]=self.data[inner_row][span[1]:].split()[0] #popula dict auxiliar
                        print(self.data[inner_row][span[0]:span[1]],end="")
                        print(self.data[inner_row][span[1]:],end='')
                    inner_row += 1
                self.pernas[i]= aux #atribui dict auxiliar em dict externo
        else:
            print("no matches")
        return self.pernas

    def getDict(self):
        print("Dict")
        for i in self.pernas:
            print("\n"+("/" * 10) + "Perna Número" + str(i + 1) + ("\\" * 10))
            for j in self.pernas[i]:
                print(j, self.pernas[i][j])
        return self.pernas

    def valBits(self):
        #print("\n"+("=" * 50))
        print('{0:=^50}'.format(''))
        print("{:^50}".format('Validação de valores coincidentes'))
        print('{0:=^50}'.format(''))
        for i in self.pernas[0].keys():
            try:
                if not (list(self.pernas[0].keys()) +
                        list(self.pernas[1].keys()) +
                        list(self.pernas[2].keys()) +
                        list(self.pernas[3].keys())
                       ).count(str(i)) == 4:
                    raise Exception
                print("Correspondência do bit: {} ------> {}".format(i,self.pernas[0][i] == self.pernas[1][i] == self.pernas[2][i] == self.pernas[3][i]))
            except:
                print("Falha ao procurar bit: {}".format(i,False))
                continue