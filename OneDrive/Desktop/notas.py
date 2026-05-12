cal= int(input("ingresa la calificacion del alumno:")) #-> esta linea sirve para ingresar la calificacion del alumno
if cal >= 7: #-> linea condicinal en la cual se define si el alumno paso
    print("aprobado")#-> en caso de haber sacado 7 se imprimira Aprobado
else:#-> segunda linea condicional la cual se activara en caso de haber tenido una calificacion debajo de 7     
    print("reprobado ")#-> en caso de haber sacado 6 se imprimira Reprobado
print("-------------------")  
    
class Carro:
    
    def __init__(self, marca, color, material):
        self.marca = marca
        self.color = color
        self.material = material 
def info(self):
    print("marca", self.marca)
    print("color", self.color)
    print("material", self.material)
    print("-------------------")    
     
Carro1 = Carro("NISSAN", "AZUL", "ACERO")
Carro2 = Carro("VERSA", "VERDE", "ALUMINIO")

info(Carro1)
info(Carro2)