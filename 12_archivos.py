# Archivos 
# ? es recomendado trabajar con la sentencia "with" que
# ? nos permite abrir un archivo y luego cerrarlo 
# ? automaticamente

with open("prueba_01.txt", "r") as archivo: 
  for linea in archivo:
    print("=====FRASE====")
    print(linea)
""" 
r = read | leer
w = write | escribir 
a = append | añadir 
+ = agregar un + incluye leer. por ejemplo w+ es escribi y leer 
 """
 
# Modificar el contenido 
notas = { 
  "A": 87, 
  "B": 97, 
  "C": 107, 
  "D": 117, 
  "E": 127
  }
with open("prueba_02.txt", "w") as archivo:
  for letter, note in notas.items():
    archivo.write(letter + " - " + str(note) + "\n")

notas_2 = { 
  "A": 187, 
  "B": 197, 
  "C": 207, 
  "D": 217, 
  "E": 227
  }

with open("prueba_02.txt", "a") as archivo:
  for letter, note in notas_2.items():
    archivo.write(letter + " - " + str(note) + "\n")