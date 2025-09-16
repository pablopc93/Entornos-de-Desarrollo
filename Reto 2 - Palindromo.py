
def es_palindromo(texto):
    return texto == texto[::-1] 
entrada = input("Introduce una palabra o frase: ")

resultado = "sí" if es_palindromo(entrada) else "no"
print(f"La frase o palabra '{entrada}' {resultado} es un palíndromo.")
