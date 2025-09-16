listas = [0,1,2]
for l in listas:
    print("l: ",l)

diccionario = {0:'a',1:'b',2:'c'}
for d in diccionario:
    print("d: ",d)

tupla = (1,2,3)
print(type(tupla))
for t in tupla:
    print("t: ", t)

del(listas[0])
print (listas)

print(diccionario.items())