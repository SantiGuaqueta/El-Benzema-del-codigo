# Punto 5 reto 5

def valor_prestamo(*args)->float:
    intereses=float
    interes_compuesto=float
    calculo_valor_del_prestamo=float
    for  calculo_valor_del_prestamo in args:
        intereses= tasa_de_interes/100 # lo dividimos entre 100 para quitar el porcentaje
        interes_compuesto=(1+intereses/12)**meses 
        calculo_valor_del_prestamo=( dinero * interes_compuesto)

    return(calculo_valor_del_prestamo)
#Planteamos la ecuaciones para hallar el calculo del valor del prestamo.

if __name__ == "__main__":
  dinero = float(input("Ingrese el valor del prestamo: ")) # Pedimos los valores
  tasa_de_interes = float(input("Ingrese la tasa de interes(sin %): ")) # Pedimos los valores
  meses = int(input("Ingrese cantidad de meses para pagar: ")) # Pedimos los valores
  print("el valor del prestamo al final es:  " + str(valor_prestamo(dinero,tasa_de_interes,meses)))
