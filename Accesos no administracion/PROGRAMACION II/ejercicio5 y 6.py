#ejercicio5
def sumar(N1,N2,N3):
    promedio=(N1+N2+N3)/3
    return promedio

    
##programa prncipal
a=int(input("ing:"))
b=int(input("ing:"))
c=int(input("ing:"))

print(sumar(a,b,c))

R=sumar(a,b,c)
print(R)



#ejercicio6    
def perimetro(N1):
    calcular=N1*4
    return calcular

#programa principal    
a=int(input("ingrese el valor de un lado del cuadrado:"))
    
print(perimetro(a))
