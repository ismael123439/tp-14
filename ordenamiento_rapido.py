def ordenamiento_rapido(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]
        return ordenamiento_rapido(menores) + iguales + ordenamiento_rapido(mayores)

print(ordenamiento_rapido([1,5,2,3,8,6,3,4,5,9,30,43,2134,43,34,43,2,5,1,8,45,634,5,3456,65,78,8456,5,63,65,645,65,5,57,7,6,6,63,64,6,546,45,645,765,75,8,68,7,672,423]));