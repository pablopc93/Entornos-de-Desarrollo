
lista = [1,2,3,4,5]

print(type(lista))
print(f"lista: {lista}")
print("lista[0]", lista[0])

lista_mezcla = [1,3.4,True,'a',"hola"]
print(f"Lista_mezcla: {lista_mezcla}")
print(f"Lista_mezcla: {lista_mezcla[4]}")

sublista = [23, [1,2,[50,60]],'hola']
print(f"Lista con sublista: {sublista}")
print(f"Sublista: {sublista[2]}")

lista_conlistas = [sublista[0],sublista[1]]
print(f"Lista con Listas de Sublista: {lista_conlistas}")
print(f"array dentro de array: {lista_conlistas[1][1]}")

lista4 = [lista[0:2], lista[2:4]]
print(f"Lista4: {lista4}")

lista_bucle = [i for i in range (10)]
print(f"lista_bucle: {lista_bucle}")
lista_bucle1 = lista_bucle[0:10:2]
print(f"Lista_bucle pares: {lista_bucle1}")
lista_bucle2 = lista_bucle[1:10:2]
print(f"Lista_bucle impares: {lista_bucle2}")
lista_bucle3 = lista_bucle[::]
print(f"Lista_bucle por defecto: {lista_bucle3}")

lista_bucle4 = lista_bucle[-1:-10:-1]
print(f"Lista_bucle al reves: {lista_bucle4}")
lista_bucle5 = lista_bucle[::-1]
print(f"Lista_bucle al reves: {lista_bucle5}")

lista_bucles = [i for i in range (100) if i % 3 == 0]
print("Lista de bucles: ", lista_bucles)

lista_bucle_letras = [1,2,3,4]
lista_bucle_letras1 = ['A','B','C','D']
lista_bucle_letras2 = [lista_bucle_letras]
lista_bucle_letras2.append(lista_bucle_letras1) #mete una lista con otros lista
print(f"listas metidas en listas: {lista_bucle_letras2}")

lista_bucle_letras2.extend(lista_bucle_letras1)
print(f"Lista con extend: {lista_bucle_letras2}")