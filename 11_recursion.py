# Recursión
# ? Definir algo en terminos de si mismo. es una función que se llama a si misma.

""" 
Funcionse recursivas 
  caso base 
  caso recursivo 
 """  

def fibonacci(n):
  # caso base
  if n == 0 or n == 1:
    return n 
  else: 
    print(n-1)
    print(n-2)
    print("######")
    # operación recursiva
    return fibonacci(n - 1) + fibonacci(n - 2) 

retorno  = fibonacci(6)
print(retorno)


def factorial(n): 
  if  n == 1 & n == 0:
    return 1 
  else: 
    print(n)
    print("#___#")
    return n * factorial(n-1)

retorno = factorial(5)
print(retorno)