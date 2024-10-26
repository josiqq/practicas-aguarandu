# https://github.com/josiqq/practicas-aguarandu/blob/main/enunciados/intermedio/2.md

def es_palindromo(text):
    text_invert = ""

    for i in text:
        text_invert = i + text_invert

    if text == text_invert:
        return True
    
    return False

print(es_palindromo("radar"))