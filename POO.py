#Ejercicio 1: Clases y Objetos
#Descripción: Crea una clase Coche que tenga los siguientes atributos: 
#marca, modelo y año. Define un método descripcion que imprima una descripción del coche.

#Ejercicio 2: Métodos y Encapsulamiento
#Descripción: Añade métodos a la clase Coche para arrancar y detener el coche, 
#así como para obtener y establecer el estado del coche (encendido o apagado).


class coche: 
    def __init__(self , marca , modelo , year): 
        self.marca = marca
        self.modelo = modelo
        self.year = year
        
    def descripcion(self): 
        return (f"la marca del carro es {self.marca}, el modelo es {self.modelo}, y el año {self.year}")
 
mi_carro = coche("mazda","r5","2004")        
print(mi_carro.descripcion())
        
        
        