from ClaseObjeto import Electrodomestico

class Lavarropa(Electrodomestico):
    __Capacidad=None
    __Velocidad=None
    __Cantidad=None
    __TipoCarga=None
    def __init__(self,Marca,Modelo,Color,Pais,Precio,Capacidad,Velocidad,Cantidad,TipoCarga):
        super().__init__(Marca,Modelo,Color,Pais,Precio)
        self.__Capacidad=Capacidad
        self.__Velocidad=Velocidad
        self.__Cantidad=Cantidad
        self.__TipoCarga=TipoCarga
    def toJSON(self):
        d = super().toJSON()["__atributos__"] #obtengo el diccionario de la superclase
        print(d)
        d.update(dict(
                    capacidadlavado = self.__Capacidad,
                    velocidadcentrifugado = self.__Velocidad,
                    cantidadprogramas = self.__Cantidad,
                    tipodecarga = self.__TipoCarga
                ))
        dL = dict(
                __class__=self.__class__.__name__,
                __atributos__= d
            )
        print(d)
        return dL
    def GetCarga(self):
        return self.__TipoCarga
    def GetImporte(self):
        Pre=self.GetPre()
        if self.__Capacidad<=5:
            Pre=Pre+(0.01*Pre)
        elif self.__Capacidad>5:
            Pre=Pre+(0.03*Pre)
        return Pre
