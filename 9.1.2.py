# Punto 4 reto 6

def vueltas(pan: int, leche: int, huevos:int, billete:float)-> float:
    return(( billete- (pan*300 + leche*3300  + huevos*350 ))) #Conocemos los valores porque el problema nos da los datos.
#Planteamos la ecuacione para hallar la vuelta de dinero.

if __name__ == "__main__":
  pan = int(input("Ingrese cantidad de panes: "))
  leche = int(input("Ingrese cantidad bolsas de leche: "))
  huevos = int(input("Ingrese cantidad de huevos: "))
  billete=float(input("Ingrese cantidad del billete: "))
  vueltas_de_dinero = lambda pan,leche,huevos,billete : billete- (pan*300 + leche*3300  + huevos*350 )
  Vueltas= vueltas_de_dinero(pan,leche,huevos,billete)
  print("las vueltas o lo que se queda debiendo es:  " + str(Vueltas))
