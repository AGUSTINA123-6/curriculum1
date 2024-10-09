##crear un programa que permita el ingreso de dos numeros enteros o decimales y resuelva las cuatro operaciones basicas de la aritmetica

def operaciones_suma():
    num1=float(input("ingrese un numero:"))
    num2=float(input("ingrese un otro numero:"))
    suma=num1+num2
    print("suma=",suma)

def operaciones_resta():
    num1=float(input("ingrese un numero:"))
    num2=float(input("ingrese un otro numero:"))
    print("resta=",resta)

def operaciones_multi():
    num1=float(input("ingrese un numero:"))
    num2=float(input("ingrese un otro numero:"))
    multi=num1*num2
    print("multi=",multi)

def operaciones_divi():
   num1=float(input("ingrese un numero:"))
   num2=float(input("ingrese un otro numero:"))
   divi=num1/num2
   print("divi=",divi)

for i in range(4):
    operaciones_suma()
    operaciones_resta()
    operaciones_multi()
    operaciones_divi()

    
i=1
while i==1:
    operaciones_suma()
    operaciones_resta()
    operaciones_multi()
    operaciones_divi()
    print("¿Queres seguir haciendo calculos?")
    print("1Si 2NO")
    i=int(input())

##n1=float(input("ingrese un numero:"))
##n2=float(input("ingrese un otro numero:"))
##suma(n1,n2)
##resta(n1,n2)
##multiplicar(n1,n2)
##dividir(n1,n2)
##
##def sumar(a,b):
##    suma=a+b
##    print(suma)
