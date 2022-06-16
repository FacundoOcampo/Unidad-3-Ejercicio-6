from ClaseObjeto import Electrodomestico

class Heladera(Electrodomestico):
    __Capacidad=None
    __Freezer=None
    __Ciclica=None
    def __init__(self,Marca,Modelo,Color,Pais,Precio,Capacidad,Freezer,Ciclica):
        super().__init__(Marca,Modelo,Color,Pais,Precio)
        self.__Capacidad=Capacidad
        self.__Freezer=Freezer
        self.__Ciclica=Ciclica
    def toJSON(self):
        d = super().toJSON()["__atributos__"] #obtengo el diccionario de la superclase
        print(d)
        d.update(dict(
                    capacidadlitros = self.__Capacidad,
                    freezer = self.__Freezer,
                    ciclica = self.__Ciclica,
                ))
        dH = dict(
                __class__=self.__class__.__name__,
                __atributos__= d
            )

        print(d)
        return dH
    def GetImporte(self):
        Pre=self.GetPre()
        if self.__Freezer==False:
            Pre=Pre+(0.01*Pre)
        elif self.__Freezer==True:
            Pre=Pre+(0.05*Pre)
        elif self.__Ciclica==True:
            Pre=Pre+(0.1*Pre)
        return Pre
