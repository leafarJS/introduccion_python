# Programación Orientada a Objetos 
# ? las clases permiten representar los atributos (valores)y funcionalidades (funciones)

class Cta_bancaria:
  def __init__(self, num_cta, name_tit, num_bal):
    self.num_cta = num_cta
    self.name_tit = name_tit
    self.num_bal = num_bal
    
    #funcionalidad retirar, depositar, generar balance, actualizar, etc
  def generar_balance(self): 
    print(self.num_bal)
  
  def depositar(self, monto):
    if monto > 0:  
      self.num_bal += monto

cuenta_1 =  Cta_bancaria("25-10-2222-355", "Jorge Callejo", 5600.50)
cuenta_2 =  Cta_bancaria("25-10-2222-356", "Rafael flores", 8600.50)
cuenta_3 =  Cta_bancaria("25-10-2222-357", "Jhonny Mamani", 15600.50)


print(cuenta_1.num_bal)
print(cuenta_2.num_cta)
print(cuenta_3.name_tit)

cuenta_3.generar_balance()

cuenta_2.depositar(10000000)

cuenta_2.generar_balance()