from enum import auto


class Persona:
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def description(self):
        print(
            "Nombre: ",
            self.nombre,
            " Edad: ",
            self.edad,
            " Residencia: ",
            self.residencia,
        )


class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad

    def description(self):
        super().description()
        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)


# Antonio = Persona("Antonio", 55, "Bolivia")
Antonio = Empleado(1500, 15, "Antonio", 55, "Bolivia")

Antonio.description()
print(isinstance(Antonio, Empleado))
print(isinstance(Antonio, Persona))
print(isinstance(Antonio, auto))
