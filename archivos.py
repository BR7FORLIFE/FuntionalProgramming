import json
import platform
import os
"""Ejercicio 1: Lectura de Archivos .txt y Generadores
Descripción: Crea un generador que lea un archivo .txt línea por línea y devuelva cada línea en mayúsculas. 
 El archivo contiene una lista de frases."""


def generador(archivo): 
    with open(archivo,"r") as archivo: 
        for frases in archivo:
            yield frases.upper()
        
archivo = "data.txt"        
for i in generador(archivo): 
    print(i)
    
"""Ejercicio 2: Escritura y Lectura de Archivos JSON
Descripción: Crea una función pura que tome una lista de diccionarios, escriba esta lista a un archivo .json 
y luego lea el archivo y devuelva la lista de diccionarios.

Define una función pura que tome una lista de diccionarios.
Escribe esta lista a un archivo .json.
Luego, lee el archivo .json y devuelve la lista de diccionarios.
Asegúrate de que la función no tenga efectos secundarios más allá de la lectura y escritura del archivo."""  

import os
import json

def clear_screen(): 
    return os.system("cls") if os.name == "nt" else os.system("clear")

def lista_diccionarios(lista): 
    print("entro")
    def agregar(lista): 
        with open("datos.json", "w") as archivo: 
            json.dump(lista, archivo, indent=4)
    
    while True:
        opcion = int(input("ver / agregar listas de diccionario/ salir?(1/2/3): "))
        if opcion == 1: 
            try:
                with open("datos.json", "r") as archivo: 
                    mostrar = json.load(archivo)
                    for i in mostrar: 
                        print(i)
            except FileNotFoundError:
                print("El archivo 'datos.json' no existe. Agrega datos primero.")
        elif opcion == 2:  
            nuevos_datos = rellenar()   
            lista.extend(nuevos_datos)
            agregar(lista)
            print("Agregado correctamente")
        else: 
            return False    

def rellenar(): 
    clear_screen()
    longitud = int(input("Cuál va a ser la longitud de la lista de diccionarios: "))
    lista = []
    for i in range(longitud): 
        diccionario = {}
        key = input("key: ")
        value = int(input("value: "))
        diccionario[key] = value
        lista.append(diccionario)
    return lista

def main(): 
    try:
        with open("datos.json", "r") as archivo:
            lista = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        lista = []
    
    while True: 
        if not lista_diccionarios(lista):
            break
    
main()

   
   
        
       