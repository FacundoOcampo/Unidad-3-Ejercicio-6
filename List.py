from Interfaz import ClaseInterface
from zope.interface import implementer
from ClaseNodo import Nodo
from ClaseHeladera import Heladera
from ClaseTelevisor import Televisor
from ClaseLavarropa import Lavarropa
@implementer(ClaseInterface)

class Lista:
    __Comienzo=None
    __Actual=None
    __Indice=0
    __Final=0
    def __init__(self):
        self.__Comienzo=None
        self.__Actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__Indice == self.__Final:
            self.__Actual=self.__Comienzo
            self.__Indice=0
            raise StopIteration
        else:
            self.__Indice+=1
            dato=self.__Actual.GetDato()
            self.__Actual=self.__Actual.GetSiguiente()
            return dato

    def AgregarAparato(self,Aparato):
        nodo=Nodo(Aparato)
        nodo.SetSiguiente(self.__Comienzo)
        self.__Comienzo=nodo
        self.__Actual=nodo
        self.__Final+=1

    #Interfaz
    def InsertarElemento(self,pos,objeto):
        Cont=1
        Cabeza=self.__Comienzo
        if self.__Comienzo is None:
            nodo=Nodo(objeto)
            nodo.SetSiguiente(self.__Comienzo)
            self.__Comienzo=nodo
            self.__Actual=nodo
            self.__Final+=1
        while Cont< pos-1 and Cabeza is not None:
            Cont+=1
            Cabeza=Cabeza.GetSiguiente()
        if pos==1:
            NuevoN=Nodo(objeto)
            NuevoN.SetSiguiente(Cabeza)
            self.__Comienzo=NuevoN
            self.__Actual=NuevoN
        else:
            NuevoN=Nodo(objeto)
            NuevoN.SetSiguiente(Cabeza.GetSiguiente())
            Cabeza.SetSiguiente(NuevoN)
        self.__Final+=1

    def AgregarElementoFinal(self,objeto):
        print("Insertando al final")
        if self.__Comienzo is None:
            NuevoN=Nodo(objeto)
            NuevoN.SetSiguiente(self.__Comienzo)
            self.__Comienzo=NuevoN
            self.__Actual=NuevoN
        else:
            Cabeza=self.__Comienzo
            while Cabeza.GetSiguiente() is not None:
                Cabeza=Cabeza.GetSiguiente()
            NuevoN=Nodo(objeto)
            Cabeza.SetSiguiente(NuevoN)
        self.__Final+=1

    def MostrarElemento(self,pos):
        Dato=None
        Cont=1
        if self.__Comienzo is None and pos!=1:
            Dato=None
        Cabeza=self.__Comienzo
        while Cabeza.GetSiguiente() is not None and Cont<pos:
            Cont+=1
            Cabeza=Cabeza.GetSiguiente()
        if Cont==pos:
            Dato=Cabeza.GetDato()
        return Dato

    def MostrarCantidades(self):
        CantL=0
        CantH=0
        CantT=0
        Cabeza=self.__Comienzo
        while Cabeza is not None:
            if type(Cabeza.GetDato()) is Heladera and Cabeza.GetDato().GetMarca()=="Philips":
                CantH+=1
            elif type(Cabeza.GetDato()) is Televisor and Cabeza.GetDato().GetMarca()=="Philips":
                CantT+=1
            elif type(Cabeza.GetDato()) is Lavarropa and Cabeza.GetDato().GetMarca()=="Philips":
                CantL+=1
            Cabeza=Cabeza.GetSiguiente()
        print("Cantidad de Heladeras de la marca Philips: {}".format(CantH))
        print("Cantidad de Televisores de la marca Philips: {}".format(CantT))
        print("Cantidad de Lavarropas de la marca Philips: {}".format(CantL))

    def MostrarL(self):
        Cabeza=self.__Comienzo
        while Cabeza is not None:
            if type(Cabeza.GetDato())==Lavarropa and Cabeza.GetDato().GetCarga()=="Superior":
                print("Lavarropa marca: {}".format(Cabeza.GetDato().GetMarca()))
            Cabeza=Cabeza.GetSiguiente()

    def MostrarTodo(self):
        Cabeza=self.__Comienzo
        while Cabeza is not None:
            print("{} {} {}".format(Cabeza.GetDato().GetMarca(),Cabeza.GetDato().GetPais(),Cabeza.GetDato().GetImporte()))
            Cabeza=Cabeza.GetSiguiente()

    def Guardar(self,Control):
        Lista=[]
        Cabeza=self.__Comienzo
        while Cabeza is not None:
            print(Cabeza)
            dato=Cabeza.GetDato()
            dicc=dato.toJSON()
            Lista.append(dicc)
            Cabeza=Cabeza.GetSiguiente()
        Control.GuardarJSONArchivo(Lista,"nuevosaparatos.json")
