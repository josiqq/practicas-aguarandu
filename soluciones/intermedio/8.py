# https://github.com/josiqq/practicas-aguarandu/blob/main/enunciados/intermedio/8.md

def numero_faltante(lista):
    lista.sort()

    for i in range(1, lista[-1] + 1):
        if not i in lista:
            print(i, end=" ")
    
numero_faltante([1, 2, 4, 5])