# https://github.com/josiqq/practicas-aguarandu/blob/main/enunciados/intermedio/9.md

def numero_mas_grande(n):
    numero = sorted(str(n), reverse=True)
    numero = "".join(numero)
    return numero

print(numero_mas_grande(123))