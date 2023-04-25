# Punto 6 reto 6

def contagiados_de_covid(dias: int, personas_contagiadas: int )-> int:
    return(2*personas_contagiadas*dias)
#Planteamos las operaciones para hallar las personas contagiadas.

if __name__ == "__main__":
  dias = int(input("Ingrese los dias que han pasado: "))
  personas_contagiadas = int(input("Ingrese cantidad de personas contagiadas: "))
  contagiados = lambda dias,personas_contagiadas:2*personas_contagiadas*dias
  conta= contagiados(dias, personas_contagiadas)
  print("El número total de personas contagiadas después de " +str(dias)+ " días es: "+str(conta))
