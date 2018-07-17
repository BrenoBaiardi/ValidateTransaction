import os,re

# def getData(NSU_row):
#     aux = {}  # cria dict auxiliar
#     print('{0:=^100}'.format(''))
#     print(NSU_row[i], end='')
#     print('{0:=^100}'.format(''))
#     start_row = data.index(NSU_row[i])
#     inner_row = start_row + 2
#     while "NSU:" not in data[inner_row]:  # enquanto não encontrar uma linha contendo outro ou o memso NSU
#         if bit_pattern.search(data[inner_row]):
#             span = bit_pattern.search(data[inner_row]).span()
#             aux[data[inner_row][span[0] + 3:span[0] + 6]] = data[inner_row][span[1]:].split()[
#                 0]  # popula dict auxiliar
#             print(data[inner_row][span[0]:span[1]], end="")
#             print(data[inner_row][span[1]:], end='')
#         inner_row += 1
#     pernas[i] = aux  # atribui dict auxiliar em dict externo
#     return pernas

NSU_row_list = []
NSU = r"NSU:001742"
# NSU = r"NSU:" + input("insira o NSU:")  # inserir NSU da transacao
NSU_pattern = re.compile(NSU)
bit_pattern = re.compile(r"(bit|cpo)\d{3}: ")
aux = []
bits = []
results = None

for filepath in os.listdir('C:/Users/breno.oliveira/PycharmProjects/BitLog/venv/logs/'):
    file = open('C:/Users/breno.oliveira/PycharmProjects/BitLog/venv/logs/' + filepath, mode="r",
                encoding="utf-8", errors='replace')
    lines = file.readlines()
    file.close()

    print("Starting search for NSU:{} in file {}...".format(NSU,filepath))

    for row in lines: # início de iteração no arquivo
        if row == lines[-1]:
            if len(aux) > 0:
                bits.append(aux)
            print("EOF - closing file {}".format(filepath))
            break
        if "NSU:" in row: #caso seja encontrado uma linha que possui um NSU QUALQUER
            # print("batata errada" + str(lines.index(row)))
            if NSU_pattern.search(row) != None: # verifica se o nsu encontrado é o esperado, ou se a linha é a ultima do arquivo
                # input("BATATA CERTA"+str(lines.index(row)))
                if len(aux) > 0:
                    bits.append(aux)
                found = True
                if results != None:
                    NSU_row_list.append(results)
                results = NSU_pattern.search(row)
                aux=[]
                aux.append(row) # coloca a primeira linha no bit (cabeçalho, com NSU)
                print("searching -> {} matches found ".format(len(NSU_row_list)) + str(results))
                print(len(NSU_row_list))
                print("aux {}".format(len(aux)))
                print("bits {}".format(len(bits)))
            else: # importante para avisar o programa que o nsu encontrado NÃO É O ESPERADO
                found = False #variável de controle
        if bit_pattern.search(row) != None and found == True: #deve se parsear somente os bits que sao DO NSU INFORMADO
            aux.append(row)



    if len(NSU_row_list)>0:
        inpt = input("Found -> {} matches... continue searching?(Y/N)".format(len(NSU_row_list)))
        if inpt.upper() == "N":
            aux=[]
            break
        if inpt.upper() == "Y": # qualquer valor que não seja "N" vai cair pra fora do laço e subir se comportando como continue
            aux=[]
            continue

for i in bits:
    for j in i:
        print(j,end='')
    # input("wait...")

print("End")