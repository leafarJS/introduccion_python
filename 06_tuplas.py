# una tupla es una estructura de datos inmutable que
# contiene una secuencia ordenada de elementos
""" 
caracteristicas:
  secuencia ordenada de valores 
  puede contener valoers de cualquier tipo de datos 
  puede contener valores de distintos tipos de datos
  cada posición de la tupla se identifica con un indice 
  es inmutable no puede ser modificada.
  NO PUEDE CAMBIAR  
 """
lista1 = (1,2,3,4,5,6,7,8,9,10)
lista2 = ("A","B","C","D","E","F","G","H","I","J")

print(lista1[2])
print(lista2[3:7])
print(lista1[0:len(lista1):2])

#encontrar un elemento ordenada
print("Z" in lista2)
print(1 in lista1)

#encontrar el indice de la tupla
print(lista1.index(7))
print(lista2.index("C"))

#contar ocurrencias 
print(lista1.count(2))
print(lista2.count("C"))