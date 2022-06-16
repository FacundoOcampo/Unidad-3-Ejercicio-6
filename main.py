from ClassMenu import Menu
from Creador import Creador
from List import Lista
if __name__=='__main__':
    NuevoMenu=Menu()
    NuevoMenu.Carga()
    Num=int(input("Seleccione una opcion:\n     1_Insertar un aparato.\n     2_Agregar un aparato a la colección.\n     3_Mostrar por pantalla qué tipo de objeto se encuentra almacenado.\n     4_Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.\n     5_Mostrar la marca de todos los lavarropas que tienen carga superior.\n     6_Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.\n     7_Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”.\n     0_Salir\n"))
    NuevoMenu.Opciones(Num)
    while Num!=0:
        Num=int(input("Seleccione una opcion:\n     1_Insertar un aparato.\n     2_Agregar un aparato a la colección.\n     3_Mostrar por pantalla qué tipo de objeto se encuentra almacenado.\n     4_Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.\n     5_Mostrar la marca de todos los lavarropas que tienen carga superior.\n     6_Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.\n     7_Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”.\n     0_Salir\n"))
        NuevoMenu.Opciones(Num)
