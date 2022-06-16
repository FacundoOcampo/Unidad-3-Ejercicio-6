class Nodo:
    __Aparato=None
    __Siguiente=None

    def __init__(self,aparato):
        self.__Aparato=aparato
        self.__Siguiente=None

    def SetSiguiente(self,siguiente):
        self.__Siguiente=siguiente

    def GetSiguiente(self):
        return self.__Siguiente

    def GetDato(self):
        return self.__Aparato
