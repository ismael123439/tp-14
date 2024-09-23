def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
    return lista

print(ordenamiento_insercion([1,5,2,3,8,6,3,4,5,9,30,43,2134,43,34,43,2,5,1,8,45,634,5,3456,65,78,8456,5,63,65,645,65,5,57,7,6,6,63,64,6,546,45,645,765,75,8,68,7,672,423]));