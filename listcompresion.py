# 1. genera numeros del 1 al 20
lista = [str(i) for i in range(21)]
print(" - ".join(lista))

# 2.  Cuadrados de números del 1 al 10
lista = [str(i**2)for i in range(11)]
print(" - ".join(lista))

# 3. Números divisibles por 3 del 0 al 30
lista = [str(i) for i in range(31) if i%3==0]
print(" - ".join(lista))

#4. Longitudes de palabras
lista = [list(range(len(lista)))]
print(lista)
