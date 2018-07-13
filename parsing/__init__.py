from Log import Log
l=Log("001742",'C:/Users/breno.oliveira/PycharmProjects/BitLog/venv/logs/')
l.getData()
#l.getDict()
l.valBits()

# import re
# import os
# bit_pattern = re.compile(r'(bit|cpo)\d{3}: ')
# # NSU:925325
# # NSU:402383
# # NSU:402386
# # NSU:000275 8 pernas
# # NSU:001654 #Não foi encontrado 07-04 11:45
# NSU=r"NSU:"+'402386' #inserir NSU da transacao
# NSU_pattern = re.compile(NSU)
#
# pernas = {}
#
# for filepath in os.listdir('C:/Users/breno.oliveira/PycharmProjects/BitLog/venv/logs/'):
#     file = open('C:/Users/breno.oliveira/PycharmProjects/BitLog/venv/logs/'+filepath,mode="r",encoding="utf-8",errors='replace')
#     data = file.readlines()
#     file.close()
#     matches=[]
#
#     for row in data:
#         if NSU_pattern.search(row):
#             matches.append(row)
#     if len(matches)==0:
#         print(NSU + " - not found in - " + filepath)
#         continue
#     elif len(matches)>=4:break
#
# if matches:
#     for i in range(len(matches)):
#         aux={} # cria dict auxiliar
#         print("=" * 100)
#         print(matches[i],end='')
#         print("=" * 100)
#         start_row = data.index(matches[i])
#         inner_row = start_row + 2
#         while "NSU:" not in data[inner_row]:#enquanto não encontrar uma linha contendo outro ou o memso NSU
#             if bit_pattern.search(data[inner_row]):
#                 span = bit_pattern.search(data[inner_row]).span()
#                 aux[data[inner_row][span[0]+3:span[0]+6]]=data[inner_row][span[1]:].split()[0] #popula dict auxiliar
#                 print(data[inner_row][span[0]:span[1]],end="")
#                 print(data[inner_row][span[1]:],end='')
#             inner_row += 1
#         pernas[i]= aux #atribui dict auxiliar em dict externo
#
#
#
#
# #######################################
# ####    print de dicionário  ##########
# #######################################
# # print("Dict")
# # for i in pernas:
# #     print("Perna Número",i+1)
# #     for j in pernas[i]:
# #         print(j, pernas[i][j])
#
# print("\n"+("=" * 100))
# print("Validação de valores coincidentes")
# print(("=" * 100)+"\n")
# for i in pernas[0].keys():
#     try:
#         if not (list(pernas[0].keys()) +
#                 list(pernas[1].keys()) +
#                 list(pernas[2].keys()) +
#                 list(pernas[3].keys())
#                ).count(str(i)) == 4:
#             raise Exception
#         print("Batimento do bit: {} ------> {}".format(i,pernas[0][i] == pernas[1][i] == pernas[2][i] == pernas[3][i]))
#     except:
#         print("Falha no Batimento do bit: {}".format(i,False))
#         continue
