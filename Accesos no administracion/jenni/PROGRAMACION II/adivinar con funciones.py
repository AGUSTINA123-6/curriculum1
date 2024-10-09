def pedir_numero():
    print("intentalo adivinar")
    estimacion1=int(input("coloca un numero"))
    return estimacion1
def comparar(estimacion2,numero2):
    if estimacion2<numero2:
        print("muy baja")
    elif estimacion2>numero2:
        print("muy alta")
        
    elif estimacion2==numero2:
        intentosRealizados=6



import random
intentosRealizados=0
print("hola, ¿como te llamas?")
miNombre=input()
numero=random.randint(1,20)
print(miNombre,"estoy pensando en un numero entre 1 y 20")
estimacion=pedir_numero()
while intentosRealizados<6:
    comparar(estimacion,numero)
    
    
    intentosRealizados=intentosRealizados+1

