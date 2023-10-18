class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

class Cliente(Persona):
    def __init__(self, nombre, apellido, numCuenta, balance):
        super(Cliente, self).__init__(nombre, apellido)
        self.numCuenta = numCuenta
        self.balance = balance

    def __str__(self):
        super(Cliente,self).__str__()+f'Número de cuenta: {self.numCuenta}, Balance: {self.balance}'

    def depositar(self, cantidad):
        if(cantidad > 0):
            self.balance += cantidad
        else:
            print('NO PUEDES INGRESAR CANTIDADES NEGATIVAS')

    def retirar(self, cantidad):
        if(cantidad > self.balance):
            self.balance -= cantidad


def crearCliente():
    name = input('Introduce el nombre de la persona')
    sur = input('Introduce el apellido de la persona')
    num = input('Introduce el número de cuenta de '+name)
    balance = input('Introduce el balance económico de '+name)
    