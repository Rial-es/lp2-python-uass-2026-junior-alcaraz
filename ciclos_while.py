""" Ejercicios de Ciclos While
Ejercicio 1: Contador ascendente
Solicite un número entero positivo e imprima todos los números desde 1 hasta dicho número utilizando un ciclo while.
Ejemplo
Entrada
5
Salida
1
2
3
4
5 """

# numero_entero = int(input("Ingrese un número entero positivo: "))
# contador = 1
# while contador <= numero_entero:
#     print(contador)
#     contador = contador + 1

#-----------------------------------------------------------------------

""" Ejercicio 2: Suma acumulada
Solicite números al usuario y acumule la suma.
El programa debe finalizar cuando el usuario ingrese el valor 0.
Al finalizar, muestre la suma total.
Ejemplo
Entrada
5
8
2
0
Salida
Suma total: 15 """

# numeros = input("Ingrese un número (0 para finalizar): ")
# suma = 0
# while numeros != "0":
#     suma += int(numeros)
#     numeros = input("Ingrese un número (0 para finalizar): ")
# print(f"Suma total: {suma}")

#-----------------------------------------------------------------------

""" Ejercicio 3: Validación de contraseña
Solicite una contraseña al usuario.
Mientras la contraseña ingresada sea diferente de:
python123
debe volver a solicitarla.
Cuando la contraseña sea correcta, muestre:
Acceso concedido
Ejemplo
Entrada
1234
admin
python123
Salida
Acceso concedido """

# contraseña = input("Ingrese una contraseña: ")
# while contraseña != "python123":
#     contraseña = input("Contraseña incorrecta. Ingrese nuevamente: ")
# print("Acceso concedido")

#-----------------------------------------------------------------------

""" Ejercicio 4: Control de asistencia
Solicite la cantidad de estudiantes presentes en cada clase.
El ingreso finalizará cuando el usuario introduzca el valor -1.
Al finalizar, mostrar:
Total de asistencias registradas.
Cantidad de clases ingresadas.
Promedio de asistencia.
Ejemplo
Entrada
25
24
27
23
-1
Salida
Total de asistencias: 99
Cantidad de clases: 4
Promedio de asistencia: 24.75 """

# cant_estudiantes = input("Ingrese la cantidad de estudiantes presentes en la clase (-1 para finalizar): ")
# total_asistencias = 0
# cant_clases = 0
# promedio_asistencia = 0
# while cant_estudiantes != "-1":
#     total_asistencias += int(cant_estudiantes)
#     cant_clases += 1
#     cant_estudiantes = input("Ingrese la cantidad de estudiantes presentes en la clase (-1 para finalizar): ")

# if cant_clases > 0:
#     promedio_asistencia = total_asistencias / cant_clases

# print(f"Total de asistencias: {total_asistencias}")
# print(f"Cantidad de clases: {cant_clases}")
# print(f"Promedio de asistencia: {promedio_asistencia}")

#-----------------------------------------------------------------------

""" Ejercicio 5: Caja registradora
Solicite el precio de los productos comprados.
El ingreso finalizará cuando el usuario ingrese 0.
Al finalizar mostrar:
Cantidad de productos.
Monto total de la compra.
Ejemplo
Entrada
15000
22000
18000
0
Salida
Productos comprados: 3
Total a pagar: 55000 """

precio_producto = input("Ingrese el precio del producto comprado (0 para finalizar): ")
cant_productos = 0
monto_total = 0

while precio_producto != "0":
    cant_productos = cant_productos + 1
    monto_total = monto_total + int(precio_producto)
    precio_producto = input("Ingrese el precio del producto comprado (0 para finalizar): ")

print(f"Productos comprados: {cant_productos}")
print(f"Total a pagar: {monto_total}")