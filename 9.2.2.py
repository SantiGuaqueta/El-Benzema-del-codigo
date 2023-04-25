# Punto 1 reto 6
from math import pi # Importamos la constante pi con el modulo math para las operaciones 
def area_perimetro_de_la_figura(*args):
    num:int=2 # Variable que coloque por gusto
    for  perimetro_figura in args: # Agregamos for
        perimetro =((num * base_rectangulo)+(num * altura_rectangulo))+ (num * pi * radio_circulo)+(num * pi * radio_circulo) # Formula del perimetro
        area=(base_rectangulo*altura_rectangulo)+(pi * radio_circulo**num)+(pi*radio_circulo**num) # Formula del area
    return(perimetro,area)
# Para hallar area o perimetro se puede buscan las formulas y las colocamos como podemos observar

if __name__ == "__main__":
  radio_circulo = float(input("Ingrese el radio de la esfera en cm: ")) # Pedimos valores
  base_rectangulo = float(input("Ingrese base del rectangulo en cm: ")) # Pedimos valores
  altura_rectangulo = float(input("Ingrese altura del rectangulo en cm: ")) # Pedimos valores
  print("El perimetro de la figura y el area de la figura es " + str(area_perimetro_de_la_figura(radio_circulo,base_rectangulo,altura_rectangulo)))
