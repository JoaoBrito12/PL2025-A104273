def processar_texto(string):
    activated = True
    sum = 0
    
    for words in string.split():
        if words.lower() == "off":
            activated = False
        elif words.lower() == "on":
            activated = True
        elif words == "=":
            print(sum)
        elif activated:
            if words.isdigit():
                sum += int(words)


string = "numeros 10 30 Off 30 On 50 = coisas 100 200 ="
processar_texto(string)
