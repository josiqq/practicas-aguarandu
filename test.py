def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    print(f"Izquierda: {izquierda}")
    print(f"Derecha: {derecha}")

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    # Compara los elementos y los agrega en orden al resultado
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agrega los elementos restantes de ambas mitades (si quedan)
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

print(merge_sort([1, 2]))