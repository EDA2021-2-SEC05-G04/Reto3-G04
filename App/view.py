"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
import model
import datetime

from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Iniciar analizador")
    print("2- Cargar datos")
    print("3- Contar los avistamientos en una ciudad")
    print("4- Contar los avistamientos por duración")
    print("5- Contar avistamientos por Hora/Minutos del día")
    print("6- Contar los avistamientos en un rango de fechas")
    print("7- Contar los avistamientos de una Zona Geográfica")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        catalog = controller.newcatalog()
    elif int(inputs[0]) == 2:
        controller.loaddata(catalog)
    elif int(inputs[0]) == 3:
        city = input("ingrese la ciudad")
        ret = controller.req1(catalog, city)
        print("numero de avistamientos: ", om.size(catalog["cities"]))
        print("numero de avistamientos en " +  city + " es : " + str(ret[0]))
        print(ret[1])
        print(ret[2])
    elif int(inputs[0]) == 4:
        lim_inf=float(input("lim inferior"))
        lim_sup=float(input("lim superior"))
        compilado,total,llave_duracion=controller.req2(catalog,lim_inf,lim_sup)
        compilado2=lt.newList("ARRAY_LIST")
        for i in range(1,4):
            elemento=lt.getElement(compilado,i)
            lt.addLast(compilado2,elemento)
        for i in range(lt.size(compilado)-2,lt.size(compilado)+1):
            elemento=lt.getElement(compilado,i)
            lt.addLast(compilado2,elemento)

        print("Hay ",total," ufos con duración máxima:",llave_duracion)
        x = PrettyTable()
        x.field_names = ["Datetime", "Country-City","State","Shape","Duration"]
        for ufo in lt.iterator(compilado2):
            x.add_row([ufo["datetime"],ufo["country"]+"-"+ufo["city"],ufo["state"],ufo["shape"],ufo["duration (seconds)"]])
        print(x)

    elif int(inputs[0]) == 5:
        hour1 = input("ingrese el limite inferior:  ")
        hour2 = input("ingrese el limite superiror:  ")
        date1 = datetime.datetime.strptime(hour1, '%H:%M:%S')
        date2 = datetime.datetime.strptime(hour2, '%H:%M:%S')
        a = controller.req3(catalog, date1, date2)
        print("el total de avistamientos entre las horas son: ",  a[0])
        print(a[1])
        print(a[2])
         
    elif int(inputs[0]) == 6:
        lim_inf=input("lim inferior en AAAA-MM-DD:\n").split("-")
        lim_sup=input("lim superior en AAAA-MM-DD:\n").split("-")
        lim_inf=datetime.date(int(lim_inf[0]),int(lim_inf[1]),int(lim_inf[2]))
        lim_sup=datetime.date(int(lim_sup[0]),int(lim_sup[1]),int(lim_sup[2]))
        primeros_ultimos,total=controller.req4(catalog,lim_inf,lim_sup)
        x = PrettyTable()
        x.field_names = ["Datetime","Date", "Country-City","State","Shape","Duration"]
        print("Hay una cantidad de :",total," ufos en este intervalo")
        for ufo in lt.iterator(primeros_ultimos):
            x.add_row([ufo["datetime"],datetime.datetime.strptime(ufo["datetime"],"%Y-%m-%d %H:%M:%S").date(),ufo["country"]+"-"+ufo["city"],ufo["state"],ufo["shape"],ufo["duration (seconds)"]])
        print(x)
    elif int(inputs[0]) == 7:
        latitudi = float(input("latitud inferior: "))
        latitudo = float(input("latitud superior: "))
        longitudi = float(input("longitud inferior: "))
        longitudo = float(input("longitud superior: "))
        map  = catalog["longitude"]
        a = controller.req5(catalog["longitude"], latitudi, latitudo, longitudi,longitudo)
        for i in lt.iterator(a):
            print("datetime : ",i["datetime"])
            print("state : ",i["state"])
            print("country : ",i["country"])
            print("shape : ",i["shape"])
            print("duration (seconds) : ",i["duration (seconds)"])
            print("latitude : ",i["latitude"])
            print("longitude" , i["longitude"])
        print(lt.size(a))
    else:
        sys.exit(0)
sys.exit(0)
