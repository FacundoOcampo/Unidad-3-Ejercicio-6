import json
from pathlib import Path
from List import Lista
from ClaseHeladera import Heladera
from ClaseLavarropa import Lavarropa
from ClaseTelevisor import Televisor
class Creador:
    def CargarAparato(self):
        lista = []
        op = None
        while op!=0:
            op = int(input("Ingrese [1]: Cargar Heladeras\nIngrese [2]: Cargar Televisor\nIngrese [3]: Cargar Lavarropa\nIngrese [0]: Para Finalizar\nIngrese Opcion-> "))
            Marca=None
            Modelo=None
            Color=None
            Pais=None
            Precio=None
            if op!=0:
                Marca=input("Ingrese la marca:")
                Modelo=input("Ingrese el modelo:")
                Color=input("Ingrese el color:")
                Pais=input("Ingrese el pais de fabricacion:")
                Precio=float(input("Ingrese el precio:"))
            if op==1:
                Cap=float(input("Ingrese la capacidad en litros:"))
                Tipo=input("Ingrese el tipo:")
                if Tipo=="Freezer":
                    Freezer=True
                    Ciclica=False
                elif Tipo=="Ciclica":
                    Freezer=False
                    Ciclica=True
                else:
                    Freezer=False
                    Ciclica=False
                H=Heladera(Marca,Modelo,Color,Pais,Precio,Cap,Freezer,Ciclica)
                lista.append(H)
            elif op==2:
                Tipo=input("Ingrese tipo de pantalla:")
                Pulg=input("Ingrese las pulgadas:")
                Def=input("Ingrese el tipo de definicion:")
                Valor=input("Ingrese si posee conexion a internet(Si/No):")
                if Valor=="Si":
                    Con=True
                else:
                    Con=False
                T=Televisor(Modelo,Marca,Color,Pais,Precio,Tipo,Pulg,Def,Con)
                lista.append(T)
            elif op==3:
                Cap=input("Ingrese la capacidad de lavado:")
                Vel=input("Ingrese la velocidad de centrifugado:")
                Cant=input("Ingrese la candidad de programas:")
                Tipo=input("Ingrese el tipo de carga:")
                L=Lavarropa(Marca,Modelo,Color,Pais,Precio,Cap,Vel,Cant,Tipo)
                lista.append(L)
            elif op==0:
                op=0
                print("Fin")
        self.GuardarJSONArchivo(lista,"Archivo.json")

    def GuardarJSONArchivo(self,Lista,Archivo):
        with Path(Archivo).open("w", encoding="UTF-8") as destino:
            json.dump(Lista, destino, indent=4)
            destino.close()

    def LeerJson(self,Archivo):
        with Path(Archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

    def CargarObjeto(self,claselista):
        ListaDicc=self.LeerJson("Archivo.json")
        for elem in ListaDicc:
            if "__class__" not in elem:
                print("No se encuentra la clase")
            else:
                class_name=elem["__class__"]
                class_=eval(class_name)
                if class_name=="Heladera":
                    atributos=elem["__atributos__"]
                    H=class_(**atributos)
                    claselista.AgregarAparato(H)
                elif class_name=="Televisor":
                    atributos=elem["__atributos__"]
                    T=class_(**atributos)
                    claselista.AgregarAparato(T)
                elif class_name =="Lavarropa":
                    atributos=elem["__atributos__"]
                    L=class_(**atributos)
                    claselista.AgregarAparato(L)

    def RetornarObjeto(self,Tipo):
        Marca=input("Ingrese la marca:")
        Modelo=input("Ingrese el modelo:")
        Color=input("Ingrese el color:")
        Pais=input("Ingrese el pais de fabricacion:")
        Precio=float(input("Ingrese el precio:"))
        if Tipo=="Heladera":
            Cap=float(input("Ingrese la capacidad en litros:"))
            Tipo2=input("Ingrese el tipo:")
            if Tipo2=="Freezer":
                Freezer=True
                Ciclica=False
            elif Tipo2=="Ciclica":
                Freezer=False
                Ciclica=True
            else:
                Freezer=False
                Ciclica=False
            Objeto=Heladera(Marca,Modelo,Color,Pais,Precio,Cap,Freezer,Ciclica)
        elif Tipo=="Lavarropa":
            Cap=input("Ingrese la capacidad de lavado:")
            Vel=input("Ingrese la velocidad de centrifugado:")
            Cant=input("Ingrese la candidad de programas:")
            Tipo2=input("Ingrese el tipo de carga:")
            Objeto=Lavarropa(Marca,Modelo,Color,Pais,Precio,Cap,Vel,Cant,Tipo2)
        elif Tipo=="Televisor":
            Tipo2=input("Ingrese tipo de pantalla:")
            Pulg=input("Ingrese las pulgadas:")
            Def=input("Ingrese el tipo de definicion:")
            Valor=input("Ingrese si posee conexion a internet(Si/No):")
            if Valor=="Si":
                Con=True
            else:
                Con=False
            Objeto=Televisor(Modelo,Marca,Color,Pais,Precio,Tipo2,Pulg,Def,Con)
        else:
            Objeto=None
            print("El tipo ingresado es incorrecto")
        return Objeto
