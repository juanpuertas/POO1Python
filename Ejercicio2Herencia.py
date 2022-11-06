class Alumno():
    def Nombre(self, nombre):
        self.nombre=nombre
    def Notas(self, notas):
        self.Notas=notas
    def Datos(self):
        print("Introduzca su nombre")
        self.nombre=input()
        print("Introduzca su nota")
        self.notas=input()
        self.notas=int(self.notas)
    def Resultado(self):
        print("Nombre del alumno: " , self.nombre, "\nNotas: " , self.notas)               
        
        if self.notas < 10:
            print("No apruebas el año")
        else:
            print("Apruebas el año")

miAlumno=Alumno()

miAlumno.Datos()
miAlumno.Resultado()
