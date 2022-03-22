class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.registro=registro
        self.precio=precio
    
    def cambiarColor(self,color2):
        if color2=="blanco" or color2=="negro" or color2=="amarillo" or color2=="verde" or color2=="rojo":
            self.color=color2

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self,registro2):
        self.registro=registro2

    def asignarTipo(self,tipo2):
        if tipo2=="gasolina" or tipo2=="electrico":
            self.tipo=tipo2

class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        Auto.cantidadCreados=cantidadCreados
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
