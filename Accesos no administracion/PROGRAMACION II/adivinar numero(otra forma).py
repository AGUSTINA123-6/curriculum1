from random import*
print("este es un juego que se trata de adivina un numero del 1 al 10")
numero=randint(1,10)
intento=int(input("ingrese un numero: "))
c=1
while c<=5 and numero!=intento:
    print("el numero es incorrecto")
    intento=int(input("vuelve a ingresar otro numero:"))
    c=c+1
    if c<=5:
        print("adivinaste")
    else:
        print("perdiste")
    break
    
    
    
    
    
