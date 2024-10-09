def MenuDeOpciones():
    print('''¿Deseas realizar otra accion?
       1- editar su nombre
       2- editar su estatura
       3- editar su año de nacimiento
       4- no quiero editar nada:''')
    opcion1=int(input("ingrese su opcion elegida:"))
    return opcion1

def calcular_edad():
    año = int(input("Para preparar tu perfil, dime en qué año naciste: "))
    edad = 2023-año-1    
    return edad

def solicitar_nombre():
    nombre=input("Para empezar, dime como te llamas:")
    return nombre

def calcular_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil, ¿Cuánto mides? Dámelo en metros: "))
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*101 )
    return estatura_cm

print("")
print("Bienvenido a ... ")
print("""
_ __
____ ___ (_) ________ ____/ /
/ __ `__ \/ / / ___/ _ \/ __ /
/ / / / / / / / / / __/ /_/ /
// // /// // \___/\__,/
""")
# Solicitud de nombre
sunombre=solicitar_nombre()
print()
print("Hola ", sunombre, ", bienvenido a Mi Red")
print()
# Cálculo de edad
fecha=calcular_edad()
print()
# Cálculo de estatura
altura=calcular_estatura()
# Cantidad de amigos
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes:"))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", sunombre,". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre: ", sunombre)
print("Edad: ",fecha,"años")
print("Estatura:", altura, "metros y", altura, "centímetros")

print("Amigos: ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Este ciclo se mantiene en ejecución hasta que el usuario desee salir
continuar="1"
while continuar=="1":
#Solicitamos opción al usuario
    escribir_mensaje=str(input("Deseas escribir un mensaje? (S/N) "))
#Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if escribir_mensaje=="S" or escribir_mensaje=="s" or escribir_mensaje=="":
        mensaje=input("Vamos a publicar un mensaje. ¿Que piensas hoy?")
        print()
        print("------------------------------------")
        print(sunombre,"dice:",mensaje)
        print("------------------------------------")
    elif escribir_mensaje=="N" or escribir_mensaje=="n":
        print("Elegiste no escribir ningun mensaje :-)")
        break
    opcion=MenuDeOpciones()
    if opcion == 1:
      sunombre=solicitar_nombre()
      print("")
    elif opcion == 2:
       altura=calcular_estatura()
       print("")
    elif opcion == 3:
       fecha=calcular_edad()
       print("")
    elif opcion == 4:
        print("Decidiste no realizar ninguna modificación en los datos")
    else:
        print("La opción ingresada es incorrecta")
        print("")
    continuar = input('''¿Deseas realizar otra acción? 1:SI /2: NO ''')
print("")
#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. ¡Hasta pronto!")
