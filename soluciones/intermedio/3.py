# https://github.com/josiqq/practicas-aguarandu/blob/main/enunciados/intermedio/3.md

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else: 
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

print(f"Entrada: {[38, 27, 43, 3, 9, 82, 10]}")
print(f"Salida: {merge_sort([38, 27, 43, 3, 9, 82, 10])}")