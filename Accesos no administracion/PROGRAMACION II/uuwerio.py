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
    año = int(input("Ingresa nuevamente el año en que naciste: "))
    edad = 2020-año-1
    
elif opcion == "4":
    print("Decidiste no realizar ninguna modificación en los datos")

else:
    print("La opción ingresada es incorrecta")

continuar = input('''¿Deseas realizar otra acción? S/N ''')
