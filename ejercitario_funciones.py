#Ejercicio 1 - Estadísticas de una lista
# def estadisticas (lista):
#     maximo = 0
#     minimo = 0
#     promedio = sum(lista) / len(lista)

#     for numero in lista:
#         if numero > maximo:
#             maximo = numero

#         if numero < minimo:
#             minimo = numero

#     return maximo, minimo, promedio
  
# #Programa principal
# numeros = [10, 20, 30, 40, 50]
# mayor, menor, promedio = estadisticas(numeros)
# print(f'El número mayor es {mayor}, el menor es {menor} y el promedio es {promedio}')


#Ejercicio 2
# def buscar(lista, valor):
#     for nombre in lista:
#         if nombre == valor:
#             return True
#     return False

# #Programa principal
# alumnos = ["Ana", "Luis", "Carlos", "Pedro", "Junior Ricardo", "Enrique"]
# nombre = input("Ingrese el nombre del alumno a buscar: ")
# resultado = buscar(alumnos, nombre)
# print(resultado)

#Ejercicio 3 -  Eliminar duplicados
# def eliminar_duplicados(lista):
#     return set(lista)

# #Programa principal
# numeros = [1, 2, 2, 3, 3, 3, 1, 2, 4]
# print(numeros_sin_duplicados)


#Ejercicio 4 - Frecuencia de elementos
# def contar_frecuencia(lista):
#     frecuencia = {}
#     for elemento in lista:
#         if elemento in frecuencia:
#             frecuencia[elemento] += 1
#         else:
#             frecuencia[elemento] = 1
#     return frecuencia

# #Programa principal
# lista = ["a", "b", "a", "c", "a", "b"]
# resultado = contar_frecuencia(lista)
# print(resultado)

#Ejercicio 5 - Promedio de notas
# def calcular_promedio(notas):
#     promedio = sum(notas) / len(notas)
#     return promedio

# def estado(promedio):
#     if promedio >= 60:
#         return "Aprobado"
#     else:
#         return "Reprobado"

# #Programa principal
# notas = [70, 80, 90, 60]
# promedio = calcular_promedio(notas)
# print(f'El promedio de las notas es {promedio} y el estado es {estado(promedio)}')

#-----------------------------------------------------------------------

#Ejercicio 6 - Agenda Telefónica
#Diccionario para agregar contactos
# agenda = {
#     "Juan": "0981123456",
#     "Maria": "0981654321",
# }
# def agregar_contacto():
#     nombre = input('Ingrese el nombre del contacto: ')
#     numero = input('Ingrese el número de teléfono: ')

#     agenda[nombre] = numero
 
#     print(f'Contacto agregado exitosamente.')

# def buscar_contacto():
#     nombre = input('Ingrese el nombre del contacto a buscar: ')
#     if nombre in agenda:
#         print(f'El número de {nombre} es {agenda[nombre]}')
#     else:
#         print(f'El contacto {nombre} no se encuentra en la agenda.')

# def mostrar_contactos():
#     if len(agenda) == 0:
#         print('No hay contactos en la agenda.')
#     else:
#         print('*\n Contactos:')
#         for nombre, numero in agenda.items():
#             print(f'{nombre}: {numero}')

# #Programa principal
# while True:
#     print('*\n === Agenda Telefónica ===')
#     print('1. Agregar contacto')
#     print('2. Buscar contacto')
#     print('3. Mostrar contactos')
#     print('4. Salir')
#     opcion = input('Seleccione una opción: ')
#     if opcion == '1':
#         agregar_contacto()
#     elif opcion == '2':
#         buscar_contacto()
#     elif opcion == '3':
#         mostrar_contactos()
#     elif opcion == '4':
#         print('Saliendo de la agenda...')
#         break
#     else:
#         print('Opción no válida.')

#-----------------------------------------------------------------------

#Ejercicio 7 - Producto más caro

# def producto_mas_caro(productos):
#     nombre = ""
#     precio_mayor = 0

#     for producto in productos:
#         if producto[1] > precio_mayor:
#             nombre = producto[0]
#             precio_mayor = producto[1]

#     return nombre, precio_mayor

# productos = [
#     ("Teclado", 150000),
#     ("Mouse", 80000),
#     ("Monitor", 1200000)
# ]

# nombre, precio = producto_mas_caro(productos)

# print("Producto:", nombre)
# print("Precio:", precio)

#-----------------------------------------------------------------------

#Ejercicio 8 - Inventario de productos

# inventario = {
#     "Teclado": 10,
#     "Mouse": 5,
#     "Monitor": 2
# }

# def agregar_stock():
#     producto = input("Ingrese el nombre del producto: ")

#     if producto in inventario:
#         cantidad = int(input("Cantidad a agregar: "))

#         if cantidad > 0:
#             inventario[producto] = inventario[producto] + cantidad
#             print("Stock agregado correctamente")
#         else:
#             print("La cantidad debe ser mayor a 0")
#     else:
#         print("Producto no encontrado")

# def vender_producto():
#     producto = input("Ingrese el nombre del producto: ")

#     if producto in inventario:
#         cantidad = int(input("Cantidad a vender: "))

#         if cantidad <= 0:
#             print("La cantidad debe ser mayor a 0")
#         elif cantidad <= inventario[producto]:
#             inventario[producto] = inventario[producto] - cantidad
#             print("Venta realizada correctamente")
#         else:
#             print("No hay suficiente stock")
#     else:
#         print("Producto no encontrado")

# def consultar_stock():
#     producto = input("Ingrese el nombre del producto: ")

#     if producto in inventario:
#         print("Stock disponible:", inventario[producto])
#     else:
#         print("Producto no encontrado")

# opcion = 0

# while opcion != 4:
#     print("\nMENU DE INVENTARIO")
#     print("1. Agregar stock")
#     print("2. Vender producto")
#     print("3. Consultar stock")
#     print("4. Salir")

#     opcion = int(input("Seleccione una opcion: "))

#     if opcion == 1:
#         agregar_stock()
#     elif opcion == 2:
#         vender_producto()
#     elif opcion == 3:
#         consultar_stock()
#     elif opcion == 4:
#         print("Finalizado")
#     else:
#         print("Opcion no válida")

#-----------------------------------------------------------------------

#Ejercicio 9 - Ranking de alumnos

# alumnos = [
#     ("Juan", 85),
#     ("Ana", 95),
#     ("Pedro", 70)
# ]

# def mejor_alumno():
#     nombre = ""
#     nota_mayor = 0

#     for alumno in alumnos:
#         if alumno[1] > nota_mayor:
#             nombre = alumno[0]
#             nota_mayor = alumno[1]
#     return nombre, nota_mayor


# def peor_alumno():
#     nombre = alumnos[0][0]
#     nota_menor = alumnos[0][1]

#     for alumno in alumnos:
#         if alumno[1] < nota_menor:
#             nombre = alumno[0]
#             nota_menor = alumno[1]
#     return nombre, nota_menor


# def promedio_general():
#     suma = 0

#     for alumno in alumnos:
#         suma = suma + alumno[1]

#     promedio = suma / len(alumnos)
#     return promedio

# mejor, nota_mayor = mejor_alumno()
# peor, nota_menor = peor_alumno()
# promedio = promedio_general()

# print("Mejor alumno:", mejor, "("+str(nota_mayor)+")")
# print("Peor alumno:", peor, "("+str(nota_menor)+")")
# print("Promedio general:", round(promedio, 2))

#-----------------------------------------------------------------------

#Ejercicio 10 - Sistema de gestión de estudiantes

estudiantes = {
    "Juan": [70, 80, 90],
    "Ana": [100, 95, 90]
}

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacio")
    elif nombre in estudiantes:
        print("El estudiante ya existe")
    else:
        notas = []

        while len(notas) < 3:
            nota = input("Ingrese una nota: ")

            if nota.isdigit():
                nota = int(nota)

                if nota >= 0 and nota <= 100:
                    notas.append(nota)
                else:
                    print("La nota debe estar entre 0 y 100")
            else:
                print("Ingrese una nota valida")
        estudiantes[nombre] = notas
        print("Estudiante agregado correctamente")

def calcular_promedio(notas):
    suma = 0

    for nota in notas:
        suma = suma + nota
    promedio = suma / len(notas)
    return promedio

def mostrar_promedios():
    for nombre in estudiantes:
        promedio = calcular_promedio(estudiantes[nombre])
        print(nombre, ":", round(promedio, 2))

def mejor_estudiante():
    nombre_mejor = ""
    promedio_mayor = -1

    for nombre in estudiantes:
        promedio = calcular_promedio(estudiantes[nombre])

        if promedio > promedio_mayor:
            promedio_mayor = promedio
            nombre_mejor = nombre

    print("Mejor estudiante:", nombre_mejor)
    print("Promedio:", round(promedio_mayor, 2))

opcion = ""

while opcion != "4":
    print("\nMENU DE ESTUDIANTES")
    print("1. Agregar estudiante")
    print("2. Mostrar promedios")
    print("3. Mostrar mejor estudiante")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_promedios()
    elif opcion == "3":
        mejor_estudiante()
    elif opcion == "4":
        print("Programa finalizado")
    else:
        print("Opcion no valida")


