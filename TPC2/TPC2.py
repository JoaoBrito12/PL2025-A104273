import re
from collections import defaultdict


def splitCSV():
    with open("obras.csv", "r", encoding="utf-8") as file:
        data = file.read()

    result = []
    field = ""
    inside_quotes = False
    i = 0

    while i < len(data):
        char = data[i]

        if char == '"':
            inside_quotes = not inside_quotes  
        elif char == ';' and not inside_quotes:
            result.append(field.strip()) 
            field = "" 
        elif char == '\n' and not inside_quotes:
            result.append(field.strip()) 
            field = ""  
        else:
            field += char 
        
        i += 1 

    if field:  
       result.append(field.strip())

    return result

def compositores_texto():
    res = []
    newK=[]

    linhas = splitCSV()
    
    i=0

    for element in linhas:
        if i<6:
            i+=1
            continue
        
        newK.append(element)

        if len(newK) == 7:
            res.append(newK[5])
            newK.clear()


    res = sorted(set(res), key=str.lower)
    return res
    
def periodo_texto():
    periodos = defaultdict(int)
    newK=[]

    linhas = splitCSV()

    i=0
    for element in linhas:
        if i < 6:  
            i+=1
            continue
        
        newK.append(element)

        if len(newK)==7:
            periodos[newK[4]] += 1 
            newK.clear()

    return dict(periodos)

def dicionario_periodo_obras():
    periodos = defaultdict(list)  
    newK=[]
    linhas = splitCSV()
    

    i = 0
    for element in linhas:
        if i < 6:  
            i += 1
            continue

        newK.append(element)
 
        
        if len(newK) == 7:
            periodos[newK[4]].append(newK[1]) 
            newK.clear()

    for periodo in periodos:
        periodos[periodo].sort() 

    return dict(periodos)
        
    
#print(compositores_texto())

resultado = compositores_texto()

with open("outputs/compositores_texto_output.txt", "w", encoding="utf-8") as f:
    for item in resultado:
        f.write(item + "\n")


#print(periodo_texto())
resultado_periodo = periodo_texto()

with open("outputs/periodo_texto_output.txt", "w", encoding="utf-8") as f:
    for periodo, count in resultado_periodo.items():
        f.write(f"{periodo}: {count}\n") 


resultado_dicionario = dicionario_periodo_obras()

with open("outputs/dicionario_periodo_obras_output.txt", "w", encoding="utf-8") as f:
    for periodo, obras in resultado_dicionario.items():
        f.write(f"{periodo}: {', '.join(obras)}\n")

#print(dicionario_periodo_obras())