class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.registro=registro
        self.precio=precio
    
    def cambiarColor(self,color):
        if color=="blanco" or color=="negro" or color=="amarillo" or color=="verde" or color=="rojo":
            self.color=color

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self,registro):
        self.registro=registro

    def asignarTipo(self,tipo):
        if tipo=="gasolina" or tipo=="electrico":
            self.tipo=tipo

class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        x=0
        for asiento in self.asientos:
            if (type(asiento)==Asiento):
                x+=1
        return x
    
    def verificarIntegridad(self):
        if self.registro==self.motor.registro:
            for asiento in self.asientos:
                if ((type(asiento)==Asiento) and (self.registro!=asiento.registro)):
                   return  "Las piezas no son originales"
            return "Auto original"


        return "Las piezas no son originales"
