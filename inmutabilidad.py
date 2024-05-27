#Título: Inmutabilidad
#Descripción: Implementa una función en Python que tome una lista como entrada y 
#devuelva una nueva lista con los elementos duplicados eliminados, sin modificar la lista original.

def inmutabilidad(lista): 
    quitar_duplicados = list(set(lista))
    return quitar_duplicados

lista = [1,2,3,4,4,4,5,6,7,7,8]
print(lista)        
print(inmutabilidad(lista))