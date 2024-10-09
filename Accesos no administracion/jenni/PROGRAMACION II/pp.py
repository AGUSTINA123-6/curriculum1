#Hola, bienvenido al programa de red social.
#Permite:
#1. Obtener datos del usuario
#2. Consultar y mostrar UN mensaje de estado del usuario
#3. Un menú de acciones del usuario.
#
#Podemos implementarlo usando un ciclo while que funcione mientras el usuario
#no escoja una acción de salida.
#Cada vez que el usuario escoja una acción podemos usar una serie de
#'if/elif/else' para ejecutar
#distintas secciones de código de acuerdo a lo que el usuario ha solicitado.
#Para empezar vamos a permitir que el usuario publique todos los mensajes que
#desee hasta que decida salir voluntariamente del programa.
############################################################
# Bienvenida
print("Bienvenido a ... ")
print("""

_ __
____ ___ (_) ________ ____/ /
/ __ `__ \/ / / ___/ _ \/ __ /
/ / / / / / / / / / __/ /_/ /
/_/ /_/ /_/_/ /_/ \___/\__,_/
""")
# Solicitud de nombre
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()
# Cálculo de edad
anio = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2020-agno-1
print()
# Cálculo de estatura
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil.¿Cuánto mides? Dámelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )
# Cantidad de amigos
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes."))

#Con los datos recolectados escribimos en pantalla un texto que resuma losdatos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre: ", nombre)
print("Edad: ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")

print("Amigos: ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Este ciclo se mantiene en ejecución hasta que el usuario desee salir
continuar = "S"
while continuar == "S":
#Solicitamos opción al usuario
 escribir_mensaje = str(input("¿Deseas escribir un mensaje? (S/N) "))
#Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "s", o nada
if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":

mensaje=input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")
elif escribir_mensaje == "N" or escribir_mensaje == "n":
print("Elegiste no escribir ningún mensaje :-) ")
opcion = input('''¿Deseas realizar otra acción?
1 - Editar su nombre
2 - Editar su altura
3 - Editar su año de nacimiento
4 - No quiero modificar ningún dato''')

if opcion == "1":

nombre = input("Ingresa nuevamente su nombre: ")

elif opcion == "2":

estatura = float(input("Ingresa nuevamente tu estatura en metros:"))

estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

elif opcion == "3":

anio = int(input("Ingresa nuevamente el año en que naciste: "))
edad = 2020-agno-1
elif opcion == "4":

print("Decidiste no realizar ninguna modificación en los datos")

else:

print("La opción ingresada es incorrecta")

continuar = input('''¿Deseas realizar otra acción? S/N ''')

#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. ¡Hasta pronto!")
