cal= int(input("ingresa la calificacion del alumno:")) #-> esta linea sirve para ingresar la calificacion del alumno
if cal >= 7: #-> linea condicinal en la cual se define si el alumno paso
    print("aprobado")#-> en caso de haber sacado 7 se imprimira Aprobado
else:#-> segunda linea condicional la cual se activara en caso de haber tenido una calificacion debajo de 7     
    print("reprobado ")#-> en caso de haber sacado 6 se imprimira Reprobado
print("-------------------")  #-> Esta linea sirve parar separar el codigo de calificaciones del codigo de objetos    

class Carro: #-> esta linea sirve para crear la clase carro
    
    def __init__(self, marca, color, material):#-> esta linea sirve para crear el constructo de la clase carro
        self.marca = marca#-> esta linea sirve para asignar el valor de marca al objeto carro
        self.color = color#-> esta linea sirve para asignar el valor de color al objeto carro
        self.material = material #-> esta linea sirve para asignar el valor de material al objeto carro

def info(self):#-> esta linea sirve para crear la funcion info en la cual se imprime la informacion del carro
    print("marca", self.marca)#-> esta linea sirve para imprimir la marca del carro
    print("color", self.color)#-> esta linea sirve para imprimir el color del carro
    print("material", self.material)#-> esta linea sirve para imprimir el material del carro
    print("-------------------")   #-> esta linea sirve para seprar la informacion de cada carro
     
Carro1 = Carro("NISSAN", "AZUL", "ACERO")#-> esta linea sirve para crear el objeto Carro1 con sus respectivos valores
Carro2 = Carro("VERSA", "VERDE", "ALUMINIO")#-> esta linea sirve para crear el objeto Carro2 con sus respectivos valores

info(Carro1)#-> esta linea sirve para llamar la funcion info e imprimir la informacion del Carro1
info(Carro2)#-> esta linea sirve para llamar la funcion info e imprimir la informacion del Carro2