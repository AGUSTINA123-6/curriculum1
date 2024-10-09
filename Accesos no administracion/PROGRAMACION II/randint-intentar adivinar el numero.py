print("este es un juego que se trata de adivinar un numero del 1 al 10...")
c=1
from random import*
Pc=randint(1,10) #randint va a designar un numero aleatorio del 1 al 10 
while c<=5 
    usuario=int(input("ingrese un numero: "))
    if Pc==usuario:
        print("felicitaciones adivinaste en el intento",c)
        break  #corta
    else:
        print("incorrecta vuelve a intentarlo")
        c=c+1
print("no lograste adivinar el numero,el numero correcto era", Pc)
