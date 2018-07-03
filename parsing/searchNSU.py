import re
import os
bit_pattern = re.compile(r'(bit|cpo)\d{3}: ')
# NSU:925325
# NSU:402383
# NSU:402386
# NSU:000275 8 pernas


NSU=r"NSU:"+'000275' #inserir NSU da transacao

for filepath in os.listdir('C:/Users/breno.oliveira/PycharmProjects/BitLog/venv/logs'):
    file = open('C:/Users/breno.oliveira/PycharmProjects/BitLog/venv/logs/'+filepath,mode="r",encoding="utf-8",errors='ignore')
    data = file.readlines()
    file.close()
    matches=[]

    for row in data:
        NSU_pattern = re.compile(NSU)
        if NSU_pattern.search(row):
            matches.append(row)
    if len(matches)==0:
        print(NSU + " - not found in - " + filepath)
        continue
    elif len(matches)>=4:break
print(matches)
if matches:
    for match in matches:
        print("=" * 100)
        print(match,end='')
        print("=" * 100)
        start_row = data.index(match)
        inner_row = start_row + 2
        while "ERROR" not in data[inner_row]:
            if bit_pattern.search(data[inner_row]):
                span = bit_pattern.search(data[inner_row]).span()
                print(data[inner_row][span[0]:span[1]],end="")
                print(data[inner_row][span[1]:],end='')
            inner_row += 1


# matches.extend(pattern.finditer(row))