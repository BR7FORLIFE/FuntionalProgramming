#Ejercicio 1: Generador de números pares
def generador_pares(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Ejemplo de uso
numero = int(input("digite un numero: "))
for numero in generador_pares(numero):
    print(numero)
    
    
#Ejercicio 2: Generador de cuadrados
def cuadrados(numrero): 
    for i in range(numero+1): 
        yield i**2
        
numero = int(input("numero: "))        
for i in cuadrados(numero): 
    print(i)
    
# Ejercicio 3: Generador de Fibonacci
def generador_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

num = int(input("numero: "))
for numero in generador_fibonacci(num):
    print(numero)

