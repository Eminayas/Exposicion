class Calculadora:
    def __init__(self, numero1, numero2):
        self.num1 = numero1
        self.num2 = numero2
    
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        multi = self.num1*self.num2
        return("{} * {} = {}".format(self.num1,self.num2,multi))
    
    def division(self):
        divi = self.num1/self.num2
        return("{} / {} = {}".format(self.num1,self.num2,divi))
    
    
    
class CalEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        
    def multiplicacion(self):
        return self.num1*self.num2 
    
    def exponente(num1,num2):
        resultado = 1
        for i in range(num2):
            resultado *= num1
        return resultado

    def valorAbsoluto(self):
        if self.num1 < 0:
            self.num1 = self.num1 * -1
        return self.num1
    
    
    
    
class CalCientifica(Calculadora):

    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
      
    PI = 3.1416 
      
    def circunferencia(self):
        cir = self.PI *self.num1
        return ("La circunferencia del valor ingresado es: {}".format(cir))
        
    def areaCirculo(self):
        ar = self.PI * (self.num1**2)
        return("El area de un circulo es: {}".format(ar))
    
    def areaCuadrado(self):
        are = self.num1 * self.num2
        return("El area de un cuadrado con los valores ingresados es: {}".format(are))
        
Cal = Calculadora
CalEst = CalEstandar
CalCin = CalCientifica        



# cal = CalEstandar(3,3)
# print(cal.exponente()) 
# print(cal.valorAbsoluto())               