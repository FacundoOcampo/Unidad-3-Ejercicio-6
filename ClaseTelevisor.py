from ClaseObjeto import Electrodomestico

class Televisor(Electrodomestico):
    __TipoP=None
    __Pulgadas=None
    __Definicion=None
    __Internet=None
    def __init__(self,Marca,Modelo,Color,Pais,Precio,Tipo,Pulgadas,Definicion,Internet):
        super().__init__(Marca,Modelo,Color,Pais,Precio)
        self.__TipoP=Tipo
        self.__Pulgadas=Pulgadas
        self.__Definicion=Definicion
        self.__Internet=Internet
    def toJSON(self):
        d = super().toJSON()["__atributos__"] #obtengo el diccionario de la superclase
        print(d)
        d.update(dict(
                    tipodepantalla = self.__TipoP,
                    pulgadas = self.__Pulgadas,
                    tipodefinicion = self.__Definicion,
                    conexionainternet = self.__Internet
                ))
        dT = dict(
                __class__=self.__class__.__name__,
                __atributos__= d
            )

        print(d)
        return dT
    def GetImporte(self):
        Pre=self.GetPre()
        if self.__Definicion=="SD":
            Pre=Pre+(0.01*Pre)
        elif self.__Definicion=="HD":
            Pre=Pre+(0.02*Pre)
        elif self.__Definicion=="FULL HD":
            Pre=Pre+(0.03*Pre)
        if self.__Internet =="Si":
            Pre=Pre+(0.1*Pre)
        return Pre
