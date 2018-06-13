#Breno César Baiardi Oliveira
#todas as tags encontradas em http://emvlab.org/emvtags/all/ foram salvas nesta lista
tags=['9F01', '9F40', '81', '9F02', '9F04', '9F03', '9F3A', '9F26', '9F42', '9F44', '9F05', '5F25', '5F24', '94', '4F', '9F06', '82', '50', '9F12', '5A', '5F34', '87', '9F3B', '9F43', '61', '9F36', '9F07', '9F08', '9F09', '89', '8A', '5F54', '8C', '8D', '5F20', '9F0B', '8E', '9F34', '8F', '9F22', '83', '9F27', '9F45', '84', '9D', '73', '9F49', '70', 'BF0C', 'A5', '6F', '9F4C', '9F2D', '9F2E', '9F2F', '9F46', '9F47', '9F48', '9F1E', '5F53', '9F0D', '9F0E', '9F0F', '9F10', '91', '9F11', '5F28', '5F55', '5F56', '42', '90', '9F32', '92', '86', '9F18', '71', '72', '5F50', '5F2D', '9F13', '9F4D', '9F4F', '9F14', '9F15', '9F16', '9F4E', '9F17', '9F39', '9F38', '80', '77', '5F30', '88', '9F4B', '93', '9F4A', '9F33', '9F1A', '9F1B', '9F1C', '9F1D', '9F35', '95', '9F1F', '9F20', '57', '98', '97', '5F2A', '5F36', '9A', '99', '9F3C', '9F3D', '9F41', '9B', '9F21', '9C', '9F37', '9F23']
found_tags = []

#bit 55 inteiro, incluindo llllvar já decodificado
chunk = '01495F2A0201245F34010182021C008407A0000000031010950580000000009A031102249B0268009C01009F02060000000000009F03060000000000009F0607A00000000310109F0802008C9F0902008C9F100706010A039000009F1A0201249F2608423158936ED6C38F9F2701809F3303E0B0C89F34034103029F3501229F360200019F3704ACAC66E89F5800DF0100DF0200DF0400'

#validação de LLLL var
LLLL = int(chunk[:4])
chunk = chunk[4:]

if len(chunk) == LLLL*2: print("Tamanho do Data Element validado com LLLL var " + str(LLLL) + " e " + str(len(chunk)) + " campos de valores")
else: print("Tamanho inconsistente com LLLL var " + str(LLLL) + " e " + str(len(chunk)) + " campos de valores")

def getTLV(dataElement):
    if len(dataElement) <= 0:
        return 0
    if dataElement[:2] in tags:
        tag = dataElement[:2]
        dataElement = dataElement[2:] #remove tag
    elif dataElement[:4] in tags:
        tag = dataElement[:4]
        dataElement = dataElement[4:] #remove tag
    else:
        print("\t Unknown tag "+dataElement[:4]+" - Not in list")
        dataElement = dataElement[6:] #remove unknown tag or value
        return getTLV(dataElement)
    print("Tag - " + str(tag), end="\t")
    
    tag_length = int(dataElement[:2],16) #tamanho do valor escrito na tag
    tag_length *= 2 #correção de tamanho significando dois chars hexa
    dataElement = dataElement[2:] #remove length
    print("Length - " + str(int(tag_length/2)), end="\t")
    
    tag_value = dataElement[:tag_length] #Valor da tag de acordo com a posição e com tamanho
    dataElement = dataElement[len(tag_value):] #remove value
    print("Value - " + tag_value)
    

    return getTLV(dataElement)#reenvia o DE

getTLV(chunk)

