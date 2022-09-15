# Errores y Excepciones que
# ? SyntaxError se un error en la sintaxis del programa.
# ? ocurre cuando no se siguen las reglas formales para
# ? escribir el código.  

# Excepción del programa
# ? Error detectado durante la ejecución del programa.
# ? ejemplo IndexError, NameError 

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))

try:
  operacion =  num1 ** num2
  print("valor 1 elevado al valor 2 da: ", operacion)
except:
  print("Error Grave")
  
try:
  salida = num1 / num2 
  print("num1 / num2 = ", salida  )
except ZeroDivisionError as e: 
  print(e)
else: # operación opcional 
  print("No se como llegamos aqui")
finally: 
  print("se ejecuta finally")  
  
  
  
  