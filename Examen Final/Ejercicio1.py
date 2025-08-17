"""1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una clase llamada Empleado donde sus atributos deben ser
nombre, edad, sueldo y de nacionalidad peruana, tendrá un metodo para
solicitar su nombre y otro para solicitar su edad. Así como un metodo
cumpleaños donde cada vez que invoque aumentará en un año la edad de la
persona.
- Crear la instancia de la clase Empleado y usar el nuevo metodo
aumentoSueldo que incrementar su sueldo en un 30% (mínimo instanciar la
clase 2 veces, mostrar por pantalla dicho sueldo ya incrementado).
- Crear un siguiente metodo prediccion() que retorne un mensaje donde
indique que: “En el año XXXX tendrá XX años”, el año se ingresará por
parámetro y la edad también, realizar una validación si la edad ingresada por
parámetro es menor a la del constructor indicar que no es posible realizar la
operación (Mostrar por pantalla este valor)"""

class Empleado:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.nacionalidad = "peruana"

    def solicitar_nombre(self):
        return self.nombre

    def solicitar_edad(self):
        return self.edad

    def cumpleaños(self):
        self.edad = self.edad + 1

    def aumento_sueldo(self):
        self.sueldo = self.sueldo + (self.sueldo * 30 / 100)

    def prediccion(self, año, edad):
        if edad < self.edad:
            print("No es posible realizar la operación")
        else:
            print("En el año " + str(año) + " tendrá " + str(edad) + " años")


# dos instancias de la clase Empleado
empleado1 = Empleado("Efrain", 25, 1000)
empleado2 = Empleado("Deysi", 30, 1500)

# sueldo incrementado
empleado1.aumento_sueldo()
empleado2.aumento_sueldo()

print(empleado1.solicitar_nombre() + " tiene un sueldo de " + str(empleado1.sueldo))
print(empleado2.solicitar_nombre() + " tiene un sueldo de " + str(empleado2.sueldo))
print("---------------------------------------")

# cumpleaños
empleado1.cumpleaños()
print(empleado1.solicitar_nombre() + " ahora tiene " + str(empleado1.solicitar_edad()) + " años")
print("---------------------------------------")

# prediccion
empleado1.prediccion(2030, 35)
empleado1.prediccion(2025, 20)
print("---------------------------------------")

# Persona que hereda de Empleado
class Persona(Empleado):
    def __init__(self, nombre, edad, sueldo, saldo):
        super().__init__(nombre, edad, sueldo)
        self.saldo = saldo

    def mostrar_saldo(self):
        print(self.nombre + " tiene un saldo de: " + str(self.saldo))

    def transferencia(self, monto, otra_persona):
        if monto > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo = self.saldo - monto
            otra_persona.saldo = otra_persona.saldo + monto
            print(self.nombre + " ha transferido " + str(monto) + " a " + otra_persona.nombre)


# personas
persona1 = Persona("Miguel", 26, 1200, 300)
persona2 = Persona("Sofia", 32, 1500, 100)

# saldo inicial
persona1.mostrar_saldo()
persona2.mostrar_saldo()

# transferencia exitosa
persona1.transferencia(200, persona2)

# saldos después de la transferencia
persona1.mostrar_saldo()
persona2.mostrar_saldo()

# transferencia con saldo insuficiente
persona2.transferencia(500, persona1)
