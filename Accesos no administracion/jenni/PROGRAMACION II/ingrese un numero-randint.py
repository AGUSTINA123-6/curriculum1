from random import*

def adivinar():
    c = 0
    numero=int(input("ingrese un numero entre 1 y 50:"))
    intento=randint(1,50)
    while c <= 5:
        if numero==intento:
            print("Adivinaste")
            c = 10
        elif intento>numero:
            c = c +1
            print("Ingresa otro número")
            intento=randint(1,intento-1)
            print(intento)
        else:
            print("Es muy chico")
            print("Ingresa otro número")
            c = c +1
            intento=randint(intento+1,50)
            print(intento)
    if c != 10:
        print ("No lograste adivinar el número")
        print ("El número era: ", numero)

adivinar()

