# https://github.com/josiqq/practicas-aguarandu/blob/main/enunciados/intermedio/1.md
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primos(n):
    primos = [i for i in range(2, n + 1) if es_primo(i)]
    return primos

print(primos(10))
