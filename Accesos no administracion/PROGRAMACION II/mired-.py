print("Bienvenido a ... ")
print("""
_ __
____ ___ (_) ________ ____/ /
/ __ `__ \/ / / ___/ _ \/ __ /
/ / / / / / / / / / __/ /_/ /
/_/ /_/ /_/_/ /_/ \___/\__,_/
""")
# Solicitud de nombre
nombre = input("Para empezar, dime como te llamas:")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()
# Cálculo de edad
año = int(input("Para preparar tu perfil, dime en qué año naciste: "))
edad = 2023-año-1
print()
# Cálculo de estatura
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil, ¿Cuánto mides? Dámelo en metros: "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*101 )
# Cantidad de amigos
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes:"))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre,". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre: ", nombre)
print("Edad: ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")

print("Amigos: ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Este ciclo se mantiene en ejecución hasta que el usuario desee salir
continuar="S"
while continuar=="S":
#Solicitamos opción al usuario
    escribir_mensaje=str(input("Deseas escribir un mensaje? (S/N) "))
#Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if escribir_mensaje=="S" or escribir_mensaje=="s" or escribir_mensaje=="":
        mensaje=input("vamos a publicar un mensaje. ¿Que piensas hoy?")
        print()
        print("------------------------------------")
        print(nombre,"dice:",mensaje)
        print("------------------------------------")
    elif escribir_mensaje=="N" or escribir_mensaje=="n":
        break
print("Elegiste no escribir ningun mensaje :-)")
opcion=input('''¿Deseas realizar otra accion?
1- editar su nombre
2- editar su estatura
3- editar su año de nacimiento
4- no quiero editar nada:''')
if opcion == "1":
    nombre = input("Ingresa nuevamente su nombre: ")

elif opcion == "2":
    estatura = float(input("Ingresa nuevamente tu estatura en metros:"))
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*101 )

elif opcion == "3":
    año = int(input("Ingresa nuevamente el año en que naciste: "))
    edad = 2020-año-1
elif opcion == "4":
    print("Decidiste no realizar ninguna modificación en los datos")

else:
    print("La opción ingresada es incorrecta")
    
continuar = input('''¿Deseas realizar otra acción? S/N ''')

#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. ¡Hasta pronto!")
