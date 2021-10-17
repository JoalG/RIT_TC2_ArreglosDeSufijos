#Genera el array con las posiciones en el texto donde se inician las palabras.
def getWordsStartPosition(text):
    res = []
    #Agrega el indice de la primera palabra
    if(len(text)>=1 and text[0] != ' '):
        res.append(0)
    #Agrega el indice de cada palabra que se encuentre despues de " "
    for i in range(1,len(text)):
        if(text[i]!=' ' and text[i-1]==' '):
            res.append(i)
    return res
