# clicos o bucles for
# ? estructura de control en programación que permite
# ? ejecutar una o varias líneas de código mútiples
# ? veces. lo usamos cuando sabemos con antelación 
# ? cuantas veces se deben repetir un cirto tipo de instrucciones 

# ! El termino iteración es primordial en este punto 

"""
Variable de control:
  variable que puede ser utilizada en el codigo que se va a repetir. 
  se actualiza automaticamente antes de cada iteración 
  debe tener un nombre descriptivo. 
"""
for i in range(4):
  print(i)
  
# range(start, stop[, step])
# start el valor del parametro por default es 0
# stop el valor del parametro stop 
# step el valor del parametro dependiendo de los saltos

# elementos iterables  
# ! listas, tuplas, diccionarios, string, sets

tupla = (1, 2, 3, 4, 5, 6, 7, 8)

persona = {
  "nombre": "Jorge", 
  "apellido": "callejo", 
  "edad": 45, 
  "masculino": True
}

for i in tupla:
  print(i)
  
for char in "LOOPS":
  print(char)
  
for num in [1,10,100,1000,10000]:
  print(num)

for clave in persona:
  print(clave)

for value in persona.values():
  print(value)
  
for clave, valor in persona.items(): 
  print(clave, valor)