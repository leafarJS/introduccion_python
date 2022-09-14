# TIPOS DE DATOS 

## NUMERICOS ##

#ENTERO
#NUMEROS QUE NO POSEEN DECIMALES 
#POSITIVOS O NEGATIVOS 
print(type(5))
print(type(-15))
print(type(0))

#NUMEROS EN COMA FLOTANTE
print(type(5.5))
print(type(5.5555))
print(type(5.0))

#VALORES BOOLEANOS
#son importantes para las expresiones condicionales y bucles
print(type(True))
print(type(False))

# ! CADENA DE CARACTERES STRING
# ? son una secuencia de caracteres encerrdos entre comillas y usados para representar texto del programa
print(type("python"))

# TODO Ejemplo
name = "Jorge Rafael Callejo flores"
print(name)
print(len(name))

#indexación 
print(name[3])

#indice inexistente
print(name[10])

name = "¡Hola, Mundo!"
print(name[6])

# ! Rebanado slid ayuda a obtener una parte de la cadena de caracteres 

print(name[1:5]) #Hola
print(name[7:12])
#variaciones en el rebanado de caracteres
print(name[0:len(name):2])
print(name[7:12:2]) #Mno

# ! Metodos de las cadenas de CARACTERES
# son operaciones comunes que vienen implementadas en python 

cadena  = "metodos con python" 
print(cadena.capitalize())
print(cadena.isalnum())
print(cadena.isalpha())
print(cadena.isdecimal())
print(cadena.isdigit())
print(cadena.islower())
print(cadena.isupper())
print(cadena.find("o"))
print(cadena.index("y"))
print(cadena.lower())
print(cadena.upper())