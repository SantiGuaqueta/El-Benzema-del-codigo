# Punto 3
def potencia_recursivo (n: float,i:int)->float:
    if i == 0:
        return(1)
    # Caso base
    else:
    # Condicion de la funcion recursiva
        return n * potencia_recursivo(n, i - 1)

if __name__ == "__main__":
  n = float(input("Ingrese numero: ")) # Pedimos numero base
  i= int(input("Ingrese exponente: ")) # Pedimos numero exponente
  potencia_del_numero = potencia_recursivo(n,i)
  print("La potencia de " + str(n) + " es " + str(potencia_del_numero))
