"""Ejercicio 1: Generador con Manejo de Excepciones
Descripción: Crea un generador que lea un archivo .txt 
línea por línea, pero maneje la excepción en caso de que el archivo no exista.

Define un generador que intente abrir y leer un archivo línea por línea.
Si el archivo no existe (FileNotFoundError), maneja la excepción e imprime un mensaje adecuado.
Usa el generador en un bucle para imprimir cada línea en mayúsculas."""

def mostrar(archivo): 
    try: 
        with open(archivo,"r") as archivo: 
            for i in archivo: 
                yield i.upper()
    except FileNotFoundError: 
        print("no se encuentra el directorio del archivo")            

archivo = "data.txt"
for i in mostrar(archivo): 
    print(i)