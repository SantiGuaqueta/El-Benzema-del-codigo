#Punto 4

num = int(input("Ingrese numero: "))# Lo dejamos afuera para que no cuente el tiempo en el que nos demoramos escribir el numero

import time #Importamos el time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
def fibo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    #print(sumFibo)
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo

if __name__ == "__main__":
  serieFibo = fibo(num)
  #print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))

end_time = time.time()

timer = end_time - start_time
print("Tiempo de ejecucion " + str(timer))
