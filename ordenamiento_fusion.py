def ordenamiento_fusion(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        ordenamiento_fusion(izquierda)
        ordenamiento_fusion(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista

print(ordenamiento_fusion([1,5,2,3,8,6,3,4,5,9,30,43,2134,43,34,43,2,5,1,8,45,634,5,3456,65,78,8456,5,63,65,645,65,5,57,7,6,6,63,64,6,546,45,645,765,75,8,68,7,672,423]));