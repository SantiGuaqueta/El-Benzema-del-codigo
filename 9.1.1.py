# Punto 3 reto 6
def cantidad_de_carne_de_aves(gallinas: int, gallos: int, pollitos:int)-> int:
    return(6*gallinas + 7* gallos+ 1* pollitos)#Conocemos que las gallinas pesan 6kg los gallos 7kg y los pollitos 1kg.
#Planteamos la ecuaciones para hallar la cantidad de carne.


if __name__ == "__main__":
  gallinas = int(input("Ingrese cantidad de gallinas: "))
  gallos = int(input("Ingrese cantidad de gallos: "))
  pollitos = int(input("Ingrese cantidad de pollitos: "))
  Cantidad_Carne = lambda gallinas,gallos,pollitos: 6*gallinas + 7*gallos + 1*pollitos # Aplicamos lambda
  Resultado = Cantidad_Carne(gallinas,gallos,pollitos)
  print("la cantidad de carne en kg es:  " + str(Resultado))
