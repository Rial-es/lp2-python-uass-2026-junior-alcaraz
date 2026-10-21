""" Ejercicio 1: Contador ascendente
Solicite un número entero positivo e imprima todos los números desde 1 hasta dicho número utilizando un ciclo for.
Ejemplo
Entrada
5
Salida 
1
2
3
4
5 """

# numero = int(input("Ingrese un número entero positivo: "))
# for i in range(1, numero + 1):
#     print(i)

#-----------------------------------------------------------------------

""" Ejercicio 2: Suma de números naturales
Solicite un número entero positivo N y calcule la suma de todos los números desde 1 hasta N.
Ejemplo
Entrada
5
Salida
La suma es: 15 """

# n = int(input("Ingrese un número entero positivo: "))
# suma = 0
# for i in range(1, n + 1):
#     suma += i
# print("La suma es:", suma)

#-----------------------------------------------------------------------

""" Ejercicio 3: Tabla de multiplicar
Solicite un número entero e imprima su tabla de multiplicar del 1 al 10 utilizando un ciclo for.
Ejemplo
Entrada
7
Salida
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70 """

# numero_entero = int(input("Ingrese un número entero: "))
# for i in range(1, 11):
#     resultado = numero_entero * i
#     print(f"{numero_entero} x {i} = {resultado}")

#-----------------------------------------------------------------------

""" Ejercicio 4: Contador de vocales
Solicite una palabra o frase e indique cuántas vocales contiene utilizando un ciclo for.
Ejemplo
Entrada
Programacion
Salida
Cantidad de vocales: 5 """

# palabra = input("Ingrese una palabra o frase: ")
# contador = 0
# vocales = "aeiouAEIOU"
# for letra in palabra:
#     if letra in vocales:
#         contador = contador + 1
# print(f"Cantidad de vocales: {contador}")

#-----------------------------------------------------------------------

""" Ejercicio 5: Triángulo de asteriscos
Solicite un número entero positivo y genere un triángulo de asteriscos utilizando un ciclo for.
Ejemplo
Entrada
5
Salida
*
**
***
****
***** """

numero = int(input("Ingrese un número entero positivo: "))
for i in range(1, numero + 1):
    print("*" * i)
