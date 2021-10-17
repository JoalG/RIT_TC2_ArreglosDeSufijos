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

#Ordena el array segun orden lexicografico de los sufijos apuntados
def sortLex(arr, text):
    
    arr.sort(key = lambda item: text[item:])
    return arr


def main():
    #Pide el texto al usuario
    text = input("Ingrese el texto a procesar: ")
    
    #Obtiene el arreglo
    arr = getWordsStartPosition(text)
    print("El arreglo con las posiciones en el texto donde se inician las palabras es:\n",arr)
    
    #Ordena el arreglo lexicograficamente
    sortedLexArr = sortLex(arr, text)
    print("El arreglo ordenado de acuerdo con el orden lexicográfico de los sufijos apuntados es:\n",sortedLexArr)


main()