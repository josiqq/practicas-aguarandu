# https://github.com/josiqq/practicas-aguarandu/blob/main/enunciados/intermedio/6.md

def longitud_maxima_subcadena(text):
    caracteres = sorted(set(text))  
    palabra = ''.join(caracteres)   
    mas_largo = ""
    
    for i in range(1, len(palabra) + 1):
        subcadena = palabra[:i]
        if subcadena in text:
            mas_largo = subcadena
    
    return mas_largo

print(longitud_maxima_subcadena("abcabcbb"))