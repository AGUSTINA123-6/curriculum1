#este es el juego de adivinar el numero
import random

intentosRealizados=0
print("")

print("¡Hola!¿Como te llamas?")
miNombre=input()
print("")

numero=random.randint(1,20)
print(miNombre,"estoy pensando un numero 1 y 20.")
print("")

while intentosRealizados <6:
    print("intenta adivinar:")
    estimacion=input()
    estimacion=int(estimacion)   
    intentosRealizados=intentosRealizados+1   

    if estimacion < numero:
        print("tu estimacion es muy baja")      
     

    if estimacion >numero:
        print("tu estimacion es muy alta")      

    if estimacion==numero:
        break    
print("")

if estimacion==numero:
    intentosRealizados=str(intentosRealizados)
    print("¡Buen trabajo, has adivinado en,", intentosRealizados,"intentos!")    
print("")

if estimacion !=numero:
    numero=str(numero)
    print("pues no. El numero que estaba pensando era "+numero)

