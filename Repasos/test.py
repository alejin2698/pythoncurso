# melo
print("Hola alejo")
print("adios alejo")
# melo
# melo
# melo

"""
    saluda al usuario
"""

print("hola perras")
print("adios perras")


name = "Alejo"
last_name = "cardona"

print("Hola " + name)
print("Tu apellido es " + last_name)


num1  = 20
num2  = 32

print("La suma es: " + str(num1 + num2))

num1 = 20.8
num2 = 5.1

result = (2+2) * (5 - num2) / 2

print("El resultado es: " + str(result))

##salud

name = "Alejo 'asc' casaaa"
apellido  = "cardona"
print(f"Hola {name} {apellido}")


## listas

list = ["Alejo", "cardona", 20, 32, 5.1]
print(list[0])
print(list[-2])

list[1] = "galeano"
print(list)

list.append("nuevo elemento")
print(list)

list.insert(1, "nuevo elemento 2")
print(list)

## tuplas

tupla = ("Alejo", "cardona", 20, 32, 5.1)
print(tupla[0])
print(tupla[-2])
# tupla[1] = "galeano"  # Esto generará un error porque las tuplas son inmutables 

##Diccionarios conocido en php como arreglos asociativos
data = {
    "nombre": "Alejo",
    "apellido": "cardona",
    "edad": 20,
    "altura": 1.75
}
print(data["nombre"])
print(data["apellido"])
print(data["edad"])
print(data["altura"])


data["ciudad"] = "Bogotá"
print(data)

del data["edad"]
print(data)

print(data.keys())
print(data.values())
print(len(data))

## entrada de datos
# name = input("Ingrese su nombre: ")
# print("Hola " + name)

# age = input("Ingrese su edad: ")
# print("Tienes " + age + " años")

# apellido = input("Ingrese su apellido: ")
# print("Tu apellido es " + apellido)

# print(f"Hola {name} {apellido}, tienes {age} años")

# nume1 = int(input("Ingrese un número: "))
# nume2 = int(input("Ingrese otro número: "))

# print(int(nume1) + int(nume2))
# print(f"La suma es: {nume1 + nume2}")
# ##funciones de numeros
# nume1float = float(input("Ingrese un número decimal: "))
# nume2float = float(input("Ingrese otro número decimal: "))
# print(f"La suma es: {nume1float + nume2float}")

# nume1int = int(input("Ingrese un número entero: "))
# nume2int = int(input("Ingrese otro número entero: "))
# print(f"La suma es: {nume1int + nume2int}")

# nume1bool = input("Ingrese un valor booleano (True/False): ")
# print(bool(nume1bool))


#if - else
# edad    = int(input("Ingrese su edad: "))
# if edad >= 18:
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")

# if not edad >= 18:
#     print("Eres menor de edad")

# if edad != 18:
#     print("No tienes 18 años")


## condicionales anidados
# edad = int(input("Ingrese su edad: "))
# if edad >= 18:
#     print("Eres mayor de edad")
#     if edad >= 65:
#         print("Eres un adulto mayor")
#     else:
#         print("Eres un adulto joven")
# else:
#     print("Eres menor de edad")
#     if edad < 13:
#         print("Eres un niño")
#     else:
#         print("Eres un adolescente")

# bucles for
numeros  = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

## tabla de multriplicar con for
table = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{table} x {i} = {table * i}")

## blucle while
count = 1
while count <= 10:
    print(f'Hola liciamigos este es mensaje {count}')
    count += 1

tabla = int (input("Ingrese un número para ver su tabla de multiplicar: "))
countmu = 1

while countmu <= 10:
    print(f"{tabla} x {countmu} = {tabla * countmu}")
    countmu = countmu + 1