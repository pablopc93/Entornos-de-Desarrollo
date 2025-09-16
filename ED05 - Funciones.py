#x2
def x2(a):
    da=2*a
    return 2*a

print("x2:", x2(2))

#x2x3
def x2x3(a):
    return 2*a, 3*a

#f1
def f1():
    varLocal = 0
    global varGlobal
    varGlobal = 200
    return var1

a = 2
a2, a3 = x2x3(a)
print("a2:", a2, "a3:", a3)
a=x2x3(a)
print(type(a), a)

#print(da) da es Local a la función x2x3
#Las variables definidas en el cuerpo de if else se pueden utilizar después
if a[0]>0:
    da=2
else:
    da=1
print(da)

#Las variables definidas en el cuerpo de for se pueden utilizar después
for i in range(5):
    suma=1
print(suma)

var1=3
#Para utilizar una variable de dentro, hay que ejecutar la función f1 para que quede definida.
print(f1())

#print(varLocal) no se puede utilizar porque está dentro de una función y es Local
#Una variable Global se puede utilizar en cualquier caso, aunque esté dentro de una función. También se puede modificar
print(varGlobal)
varGlobal=300
print(varGlobal)

x = lambda a, b: a + b
print(x(1, 1))

#factorial
def factorial(num):
    factorial = 1
    for i in range(2, num+1):
        factorial += i
    return factorial

def factorialR(num):
    if num ==1:
        return 1
    else:
        return num*factorial(num-1)



print(factorial(5))  
print(factorialR(5))  