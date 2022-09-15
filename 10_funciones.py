# funciones
# ? bloque de instrucciones reutilizable que realiza
# ? una sola tarea especifica. Don't repeat yourself (DRY)

""" Ventajas:
  reusable 
  consiso 
  leible 
  mantenible 
  comprobable 
 """
def mensaje():
  print("!Hola mundo¡")
  
mensaje()

# parámetros 
# ? es una varibable que se incluye en la definición de
# ? la función para representar y guardar un valor que
# ? podemos pasar cuando llamamos a la función. 

def mostrar_doble(num): 
  print(num * 2)

mostrar_doble(100)

# ? si existen mas de un parametro se separa con una coma

def sumar(x, y):
  print(x + y)

sumar(1000 , 9999)

# Argumentos de la función 
# ? valor que asignamos a un parametro cuando llamamos a la función
arg_1 = 5
arg_2 = 10

def exponente(x, y):
  print(x**y)

exponente(arg_1, arg_2) 

# Proposito
# ?  retornar un valor luego de completar el codigo o la tarea. 
def operacion(x, y):
  i = x 
  for i in range(y):
    i+= 1
    print(i)
    
  if i == y: 
    return True
  else: 
    return False 
  
# ? cuando se ejecuta la sentencia return la ejecución
# ? se detiene inmediatamente, en caso de no existir un
# ? retorno, por defecto devuelve el valor NONE
retorno = operacion(1, 11)
print(retorno)

# TODO: en el sell interactivo, el valor retornado por la llamada a una función no se muestra si se asigna a una variable.

# alcance de una variable (scope)
# ? alcance que tendra la variable en el programa. 
# ? Dónde se podrá usar. Se determina el alcance, hay 2 tipos de alcace, global y local.

var_global = 100 

def func(x):
  print(x)
  var_local = 10 
  return var_global ** var_local

retorno = func("Soy un argumento pero no me utilizaran")
print(retorno)




