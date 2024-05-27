#Funciones Puras

#1. Descripción: Escribe una función en Python que determine si un número es primo o no. 
# La función debe ser pura, es decir,no debe realizar ningún efecto secundario observable.


#funcion pura
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            i += 6
        return True


print("primo?: ",es_primo(17))  # True
print("primo?: ",es_primo(15))  # False

#Verificar Palíndromos
#Descripción del Ejercicio: Escribe una función en Python que determine si una cadena de texto es un palíndromo o no. 
#La función debe ser pura, es decir, no debe realizar ningún efecto secundario observable.

def palindromo(palabra): 
    return True if palabra == palabra[::-1] else False

print("\nPalindromo?: ",palindromo("oso"))
print("\nPalindromo?: ",palindromo("palabra"))

#Generar Secuencia Fibonacci 
def secuencia_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:n]
print(secuencia_fibonacci(10))  

# factorial

def factorial(numero): 
    if numero == 0 or numero ==1: 
        return 1
    else: 
         numero = numero * factorial(numero-1)
         return numero
print("factorial?: ",factorial(5))        
        
    
