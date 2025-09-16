"""
a=50

if a%2==0:
    print(f"El valor {a} es par")
else: 
    print(f"El valor {a} es impar")

if a>50:
    print(f"El valor {a} es mayor a 50")
elif a<50:
    print(f"El valor {a} es menor de 50")
else:
    print(f"El valor {a} es igual a 50")

num = input("Introduce un numero: ")
print("Valor introducido",num)

num=int(num)
b=0
while b<num:
    print("B: ",b)
    b+=1


#bucle q  solicite numeros al usuario hasta introducir un numero par

num1 = input("Introduce un numero: ")
num1 = int(num1)
while num1%2 != 0:
    num1 = input("Introduce otro  numero: ")
    num1 = int(num1)

print(f"{num1} es par")

#bucle for
sum=0
for c in range (10):
    sum+=c
    print("C: ",c ,", sum: ",sum)
"""
#consecutivos, bucle q num al usuairo hasta q salgan 2 numeros seguidos q sean pares
num2 = int(input("Introduce el primer número: "))
num3 = int(input("Introduce el segundo número: "))
while:
    num2 = int(input("Introduce el primer número: "))
    num3 = int(input("Introduce el segundo número: "))
    
  

