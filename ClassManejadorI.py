from Interfaz import ClaseInterface
from List import Lista
from Creador import Creador
class ManI:
    __Control=Creador()
    def __init__(self):
        self.__Control=Creador()

    def InvocarInter(self,CLista:ClaseInterface,op):
        if op==1:
            pos=int(input("Ingrese la posicion:"))
            tipo=input("Ingrese un tipo de aparato:")
            objeto=self.__Control.RetornarObjeto(tipo)
            if objeto is not None:
                CLista.InsertarElemento(pos,objeto)
            else:
                print("El elemento a insertar no es un objeto")
        if op==2:
            aparato=input("Ingrese el tipo de aparato:")
            objeto=self.__Control.RetornarObjeto(aparato)
            if objeto is not None:
                CLista.AgregarElementoFinal(objeto)
            else:
                print("El elemento a insertar no es un objeto")
        if op==3:
            pos=int(input("Ingrese una posicion de la lista:"))
            dato=CLista.MostrarElemento(pos)
            if dato is not None:
                print(repr(dato))
            else:
                print("Posicion incorrecta")
    def LLamarInterfaz(self,CLista,op):
        self.InvocarInter(ClaseInterface(CLista),op)
