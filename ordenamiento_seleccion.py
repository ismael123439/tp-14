def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

print(ordenamiento_seleccion([1,5,2,3,8,6,3,4,5,9,30,43,2134,432,423]));