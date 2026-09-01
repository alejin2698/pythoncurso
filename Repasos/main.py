from Clases.carro import Carro, Carro4X4, CarroDeportivo  

# class Carro:
#     pass 
#     marca = ""
#     color = "Gris"
#     modelo = ""
#     __encendido = False
#     velocidad = 0

#     def __init__(self, marca, color, modelo):
#         self.marca = marca
#         self.color = color
#         self.modelo = modelo

#     def encender(self):
#         self.__encendido = True

#     def set_velocidad(self, velocidad):
#         self.velocidad = velocidad

#     def get_encendido(self):
#         return self.__encendido

# class Carro4X4:
#     size_ruedas = 18

# class CarroDeportivo(Carro, Carro4X4):
#     caballos = 60

#     def __init__(self, marca, color, modelo, caballos, size_ruedas):
#         self.marca = marca
#         self.color = color
#         self.modelo = modelo
#         self.caballos = caballos
#         self.size_ruedas = size_ruedas



## Aqui llamamos cada objecto

carro1 = Carro("Mazda", "Rojo", "Cx-30")
carro2 = Carro("Toyota", "Azul", "Corolla")
carro3 = CarroDeportivo("Ferrari", "Rojo", "F8", 600, 20)

print(f'El carro1 es de marca {carro1.marca}, color {carro1.color} y modelo {carro1.modelo}')
print(f'El carro2 es de marca {carro2.marca}, color {carro2.color} y modelo {carro2.modelo}')
print(f'El carro3 es de marca {carro3.marca}, color {carro3.color}, modelo {carro3.modelo} y tiene {carro3.caballos} caballos de fuerza. El tamaño de las llanas son de {carro3.size_ruedas} pulgadas')

carro1.color = "Negro"
print(f'se le dio la regalada gana de cambiar el color del carro1 por: {carro1.color}')

# Aqui enceiende el carro1
carro1.encender()
carro1.set_velocidad(60)

if carro1.get_encendido():
    print('El carro1 está encendido y tiene una velocidad de: ', carro1.velocidad)
else:
    print('El carro1 está apagado')

# Aqui enceiende el carro2
carro2.encender()
carro2.set_velocidad(80)

if carro2.get_encendido():
    print('El carro2 está encendido y tiene una velocidad de: ', carro2.velocidad)
else:
    print('El carro2 está apagado')

# Aqui enceiende el carro3
carro3.encender()
carro3.set_velocidad(200)

if carro3.get_encendido():
    print('El carro3 está encendido y tiene una velocidad de: ', carro3.velocidad)
else:
    print('El carro3 está apagado')
