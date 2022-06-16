from Creador import Creador
from List import Lista
from ClassManejadorI import ManI

class Menu:
    __Switch=None
    def __init__(self):
        self.__Switch={
            1:self.Opcion1,
            2:self.Opcion2,
            3:self.Opcion3,
            4:self.Opcion4,
            5:self.Opcion5,
            6:self.Opcion6,
            7:self.Opcion7,
            0:self.Salir
        }
        self.__Nuevoc=Creador()
        self.__ClassLista=Lista()
        self.__ManI=ManI()

    def Opciones(self,Num):
        Fun=self.__Switch.get(Num,lambda : print("Opcion Incorrecta"))
        if Num>=0 and Num<=7:
            Fun()
        else:
            Fun()

    def Carga(self):
        #self.__Nuevoc.CargarAparato()
        self.__Nuevoc.CargarObjeto(self.__ClassLista)





    def Opcion1(self):
        self.__ManI.InvocarInter(self.__ClassLista,1)
    def Opcion2(self):
        self.__ManI.InvocarInter(self.__ClassLista,2)
    def Opcion3(self):
        self.__ManI.InvocarInter(self.__ClassLista,3)
    def Opcion4(self):
        self.__ClassLista.MostrarCantidades()
    def Opcion5(self):
        self.__ClassLista.MostrarL()
    def Opcion6(self):
        self.__ClassLista.MostrarTodo()
    def Opcion7(self):
        self.__ClassLista.Guardar(self.__Nuevoc)
    def Salir(self):
        print("Se salio con exito")
