# diccionarios 
# ? colección de pares clave - valor 

""" 
Caracteristicas:
  coleccion de pares clave-valor 
  las claves deben ser unicas e inmutables con
  los valores asociados pueden ser de cualquier tipo 
  la clave se usa para acceder a su valor asociado 
  los pares clave valor pueden ser modificados, añadidos y eliminados 
"""
persona = {
  "nombre": "Jorge", 
  "apellido": "callejo", 
  "edad": 45, 
  "masculino": True
}
#acceder por clave 
print(persona["nombre"])
print(persona.get("edad"))

#modificar 
persona["nombre"] = "jorge Rafael"
persona["apellido"] = "callejo flores"

#añadir
persona["estado"] = "soltero"

#remover un par del diccionario 
del persona["masculino"]

#revisar la existencia de un elemento  
print("edad" in persona)

print(persona)