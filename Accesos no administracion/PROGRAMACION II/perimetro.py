##definir una funcion que resuelva el perimetro del cuadrado o rectangulo e indique de que figura se trata

def calcular_peri(L1,L2):
    perimetro=L1*2+L2*2
    return perimetro 
  
##prog. principal
a=float(input("1° lado:"))
b=float(input("2° lado:"))
r=calcular_peri(a,b)
print(calcular_peri(a,b))

if a==b:
    print("es un cuadrado")
else:
    print("es un rectangulo")  
