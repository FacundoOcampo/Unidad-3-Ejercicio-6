class Electrodomestico:
    __Marca=None
    __Modelo=None
    __Color=None
    __Pais=None
    __Precio=None
    def __init__(self,Marca,Modelo,Color,Pais,Precio):
        self.__Marca=Marca
        self.__Modelo=Modelo
        self.__Color=Color
        self.__Pais=Pais
        self.__Precio=Precio
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    marca=self.__Marca,
                    modelo = self.__Modelo,
                    color = self.__Color,
                    paisdefabrica = self.__Pais,
                    precio = self.__Precio
                )
            )
        return d
    def GetMarca(self):
        return self.__Marca
    def GetPais(self):
        return self.__Pais
    def GetPre(self):
        return self.__Precio
