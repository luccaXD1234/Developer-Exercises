import math 
import sys

class Circulos :
    def __init__(self, radio):
        self.radio = radio
    def __str__(self):
        return("\nya creamos un circulo nuevo con un radio de "f"{self.radio}""cm , ahora calcularemos el area y el perimetro ")


    def area(self):
        resultadoA =math.pi*self.radio**2
        return resultadoA
    
    def Perimetro(self):
        resultadoP=math.pi*2*self.radio
        return resultadoP

    def calc(self):
        resultadoC = self.radio * n
        return resultadoC


# Crear una instancia de la clase Sumadora con los números 5 y 7

print("\n\nvoy a calcular el perimetro y area de un circulo por usted ")
r=int(input("ingrese el radio : "))
if r==0:
    print(  "\n\n----error---- \nno podremos hacer su calculo ya que ingreso un 0 y no se puede calcular el radio, ni el perimetro  ")
    sys.exit()
if r<0:
    print(  "\n\n----error---- \nno podremos hacer su calculo ya que ingreso un numero negrativo y no se puede calcular el radio ni el perimetro  ")
    sys.exit()
circulo1 = Circulos(r)


# llamar metodos 
resultadoA = circulo1.area()
resultadoP = circulo1.Perimetro()

# ver si se quiere multiplicar el r por algun numero 

m=int(input("ingrese 1 si desea multiplicar el circulo por un numero, si no cualquier otro valor : "))
if m ==1:
    n=int(input("ingrese el numero que quiere multiplicar por el radio"))
    resultadoC= circulo1.calc()
    print("\nel resultado del radio por su numero es :",resultadoC )


#imprimir 
print(circulo1)       
print("Area :" ,resultadoA)
print("Perimetro :",resultadoP)





