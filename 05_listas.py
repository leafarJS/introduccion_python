# listas
# ? Estructura de datos utilizada para almacenar
# ? multiples valores en secuencia 
""" 
caracteristicas:
  -secuencia ordenada de valores 
  -pueden contener valores de cualquier tipo 
  -cada posición en la lista esta asociada a un entero llamado indice
  -lo principal es que son mutables. 
"""
letras = ["A","B","C","D","E","F","G","H","I","J", "K"]
letras2 = [0,1,2,3,4,9,8,7,6,5]

print(letras[2])
print(letras[3:7])
print(letras[0:len(letras):2])

#agregar al final de la lista 
letras.append("L")

#agregar en un indice especifico 
letras.insert(3,"CH")

print(letras)

#remover un elemento

letras.remove("CH")

# encontrar un elemento 
print("D" in letras)
print("Z" in letras)

#Index, retorna el indice de la primera ocurrencia 
print(letras.index("F"))

#cambiar un elemento es posible porque son mutables 
letras[8] = 666

print(letras)

# ! METODO DE LAS LISTAS 
# ? operaciones comunes de listas que ya estan 
# ? implementadas en python

print(letras.count("A"))
print(letras.extend(letras2))
print(letras2.pop())
print(letras2.reverse())
print(letras2.sort())