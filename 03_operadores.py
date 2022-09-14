# Operador son simbolos que denotan una operacion 
# en el programacion
# ! operador + operandos  = expresión

#una expresión es una convinación de valores y 
# variables y operadores que al ser evaluados 
# resultan en un valor 

# las expresiones se evaluan de izq a der mayormente
#excepto cuando ciertos operadores tienen mayor importancia

# Operadores Aritmeticos 
# ? permiten realizar suma, resta, producto, división 
# ? división entera, exponente, módulo 

num1  = 5 
num2 = 10

print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 % num2)
print(num1 * num2)
print(num1 ** num2)
print(num1 ^ num2)
print(num1 // num2) # se utiliza en una busqueda binaria

# Operadores logicos 
# ? nos permiten trabajar con valores booleanos True y False
# ? (and) evalua si el operdor izq y el operador der son verdaderos 
# ? (or) evalua que por lo menos un operador sea verdadero 
# ? (not) negar una operador verdadero  

print((5 < 6) and (7 < 8))
print((5 < 6) and (7 > 8))

print((5 < 6) or (7 < 8))
print((5 < 6) or (7 > 8))

print(not True)
print(not False)

# ! prioridad de mayor a menor not and or

# Operadores relacionales 
# ?  son utilizados para comparar valores y retornar 
# ? un valor booleano , esos operadoers son , mayor que >
# ? menor que <, mayor igual que >=, menor igual que <=, 
# ? igual ==, diferente !=

print(num1 < num2)
print(num1 <= num2)
print(num1 > num2)
print(num1 >= num2)
print(num1 == num2)
print(num1 != num2)

# Operadores de asignación
# ? son utilizados par asignar valores a las
# ? variables del programa
"""
=
+=
-=
/=
**=
// =
%=

 """
num3 = 10
print("parto del numero")
print(num3)

num3 += 10
print(num3)

num3 -= 10
print(num3)

num3 /= 10
print(num3)

num3 **= 10
print(num3)

num3 %= 10
print(num3)




