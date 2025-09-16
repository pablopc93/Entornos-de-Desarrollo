def factorialI(n):
    factorial = 1
    for i in range(2,n+1):
        print("I:",i)
        factorial*=i
    return factorialI

def factorialR(m):
    if m<0:
        raise TypeError("No se puede obtener el factorial de valores negativos")
    if m<=1:
        return 1
    else:
        return m* factorialR(m-1)

#funcion iterativa q reice una lista cuyos ele,entos son listas de enteros
#La funcion devuelve la suma de los valores de todas las listas
def sumalistaI(l):
    sumTotal = 0
    for i in l:
        sumTotal+=sum(i)
    return sumTotal


lista = [[10,2,4],[100,6,90],[1,1,14],[2,2,2],[456,4],[40]]
print("SumaLista: ",sumalistaI(lista))

#mismo q sublistal sin sum
def sumaLista2I(l):
    sumTotal = 0
    for i in l:
        for j in i:
            sumTotal+=j
    return sumTotal

print("SumaLista2I: ",sumaLista2I(lista))

def sumLista2R(l):
    if len(l) == 0:
        return 0
    else:
        return sum(l)

print("SumaLista2R(lista): ",sumLista2R(lista))

"""
print("FactorialI (4): ",factorialI(4))
print("FactorialR (4): ", factorialR(4))
"""