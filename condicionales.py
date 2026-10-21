""" Ejercicio 1: Control de acceso
Solicite al usuario su edad y si posee documento de identidad (S/N).
Permitir el ingreso únicamente si:
-Tiene 18 años o más.
-Posee documento de identidad.
En caso contrario, informar el motivo por el cual no puede ingresar. """

# edad = int(input("Ingrese su edad: "))
# documento = input("¿Posee documento de identidad? (S/N): ")
# if edad >= 18 and documento.upper() == "S":
#     print("Ingreso permitido, adelante")
# else:
#     print("No puede ingresar, no posee la edad minima requerida o no posee documento de identidad.")
#     if edad < 18:
#         print("No puede ingresar: No cumple con la edad minima requerida.")
#     if documento.upper() != "S":
#         print("No puede ingresar: No posee Documento de identidad.")

#-----------------------------------------------------------------------

"""Ejercicio 2: Descuento en una tienda
Solicite el monto de una compra.
Aplicar los siguientes descuentos:
20% si supera Gs. 500.000
10% si supera Gs. 200.000
Sin descuento en cualquier otro caso
Mostrar:
Monto original
Descuento aplicado
Total a pagar """

# compra = float(input("Ingrese el monto de la compra (Gs.): "))
# if compra > 500000:
#     descuento = compra * 0.20
# elif compra > 200000:
#     descuento = compra * 0.10
# else:
#     descuento = 0
# total = compra - descuento
# print(f"Monto original: Gs. {compra}")
# print(f"Descuento aplicado: Gs. {descuento}")
# print(f"Total a pagar: Gs. {total} Gs.")

#-----------------------------------------------------------------------

""" Ejercicio 3: Semáforo inteligente
Solicite el color del semáforo:
Verde
Amarillo
Rojo
Mostrar la acción correspondiente:
Avanzar
Reducir velocidad
Detenerse
Si el color ingresado no es válido, muestre un mensaje de error. """

# color = input("Ingrese el color del semáforo (Verde/Amarillo/Rojo): ")
# if color.lower() == "verde":
#     print("Avanzar")
# elif color.lower() == "amarillo":
#     print("Reducir velocidad")
# elif color.lower() == "rojo":
#     print("Detenerse")
# else:
#     print("Error: El color del semáforo no esválido.")

#-----------------------------------------------------------------------

""" Ejercicio 4: Nivel de batería
Solicite el porcentaje de batería de un teléfono móvil.
Mostrar:
Crítica (0% a 10%)
Baja (11% a 30%)
Normal (31% a 80%)
Alta (81% a 100%)
Validar que el porcentaje ingresado sea correcto. """

# bateria = int(input("Ingrese el porcentaje de la batería del telefono (0-100): "))
# if bateria < 0 or bateria > 100:
#     print("Error: Porcentaje de batería no válido tiene que ser un número entre 0 y 100.")
# elif bateria <= 10:
#     print("Nivel de batería: Crítica")
# elif bateria <= 30:
#     print("Nivel de batería: Baja")
# elif bateria <= 80:
#     print("Nivel de batería: Normal")
# else:
#     print("Nivel de batería: Alta")

#-----------------------------------------------------------------------

""" Ejercicio 5: Evaluación climática
Solicite la temperatura actual.
Mostrar:
Mucho frío (menos de 10°C)
Templado (10°C a 24°C)
Caluroso (25°C a 34°C)
Muy caluroso (35°C o más) """

temperatura = float(input("Ingrese la temperatura actual (°C): "))
if temperatura < 10:
    print("Mucho frío")
elif temperatura <= 24:
    print("Templado")
elif temperatura <= 34:
    print("Caluroso")
else:  
    print("Muy caluroso")