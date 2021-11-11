"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
import datetime
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mk
assert cf
def catalog():
    ufos = {
        "ufo" : None,
        "cities" :None,
        "hour" : None
    }
    ufos['Duración'] = om.newMap(omaptype="BST",comparefunction=comparador_Segundos)
    ufos["Fecha"]=om.newMap(omaptype="BST",comparefunction=comparador_Segundos)
    ufos["hour"] = om.newMap ("BST")
    ufos["ufo"] = lt.newList("ARRAY_LIST")
    ufos["cities"] = om.newMap("BST")
    return(ufos)

def req2(analyzer,lim_inf,lim_sup):
    omap_duracion=analyzer["Duración"]
    lista_listas=om.values(omap_duracion,lim_inf,lim_sup)
    iterador=lt.iterator(lista_listas)
    compilado=lt.newList("ARRAY_LIST")
    for omap in iterador:
        valueset=om.valueSet(omap)
        for lista in lt.iterator(valueset):
            for ufo in lt.iterator(lista):
                lt.addLast(compilado,ufo)
    mayor_duración_llave=om.maxKey(omap_duracion)
    valor=me.getValue(om.get(omap_duracion,mayor_duración_llave))
    valor=om.valueSet(valor)
    cantidades=0
    for lista in lt.iterator(valor):
        cantidades+=lt.size(lista)
    
    return compilado,cantidades,mayor_duración_llave

def req4(analyzer,lim_inf,lim_sup):
    omap_duracion=analyzer["Fecha"]
    lista_listas=om.values(omap_duracion,lim_inf,lim_sup)
    compilado=lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista_listas):
        for e in lt.iterator(i):
            lt.addLast(compilado,e)
    compilado=mk.sort(compilado,comparador_algo_ord)
    compiladov2=lt.newList("ARRAY_LIST")
    for i in range(1,4):
        elemento=lt.getElement(compilado,i)
        lt.addLast(compiladov2,elemento)
    for i in range(lt.size(compilado)-2,lt.size(compilado)+1):
        elemento=lt.getElement(compilado,i)
        lt.addLast(compiladov2,elemento)
    total=lt.size(compilado)
    return compiladov2,total
def comparador_algo_ord(el1,el2):
    fecha=hacer_fecha(el1)
    fecha2=hacer_fecha(el2)
    return fecha<fecha2
def hacer_fecha(fecha):
    fecha1=(fecha["datetime"].split(" ")[0]).split("-")
    fecha2=((fecha["datetime"].split(" "))[1]).split(":")
    fechax=datetime.datetime(int(fecha1[0]),int(fecha1[1]),int(fecha1[2]),int(fecha2[0]),int(fecha2[1]),int(fecha2[2]),0)
    return fechax
def addufo(catalog, ufo):
    lt.addLast(catalog["ufo"], ufo)
    update(catalog["cities"], ufo)
    updatehour(catalog["hour"], ufo)
def comparador_Segundos(ob1,ob2):
    if (ob1 == ob2):
        return 0
    elif (ob1 > ob2):
        return 1
    else:
        return -1
def addUfoDuracion(catalog, avist):
    omap=catalog["Duración"]
    duración=float(avist["duration (seconds)"])
    contiene=om.contains(omap,duración)
    if contiene:
        valor1=me.getValue(om.get(omap,duración))
        llave2=avist["country"]+"-"+avist["city"]
        contiene2=om.contains(valor1,llave2)
        if contiene2:
            valor2=me.getValue(om.get(valor1,llave2))
            lt.addLast(valor2,avist)
        else:
            lista=lt.newList("ARRAY_LIST")
            lt.addLast(lista,avist)
            om.put(valor1,llave2,lista)
    else:
        valor=crear_estructura_valor(avist)
        om.put(omap,duración,valor)
def crear_estructura_valor(avist):
    lista_avist=lt.newList("ARRAY_LIST")
    lt.addLast(lista_avist,avist)
    om_ciudad=om.newMap(omaptype="RBT",comparefunction=comparador_alfabético)
    llave=avist["country"]+"-"+avist["city"]
    om.put(om_ciudad,llave,lista_avist)
    return om_ciudad

def comparador_alfabético(country1_ciudad1,country2_ciudad2):
    primer_caracter=ord(str(country1_ciudad1[0]).lower())
    segundo_caracter=ord(str(country2_ciudad2[0]).lower())
    if (primer_caracter == segundo_caracter):
        return 0
    elif (primer_caracter > segundo_caracter):
        return 1
    else:
        return -1

def addUfoFecha(catalog,avist):
    omap=catalog["Fecha"]
    fecha=(avist["datetime"].split(" ")[0]).split("-")
    fecha=datetime.date(int(fecha[0]),int(fecha[1]),int(fecha[2]))
    contiene=om.contains(omap,fecha)
    if contiene:
        existe=me.getValue(om.get(omap,fecha))
        lt.addLast(existe,avist)
    else:
        valor=lt.newList()
        lt.addLast(valor,avist)
        om.put(omap,fecha,valor)
def updatehour(map, ufo):
    ho = ufo["datetime"][11:]
    ho = datetime.datetime.strptime(ho, '%H:%M:%S')
    index = om.get(map, ho)
    if index is None:
        ma = newufoh()
        om.put(map, ho,ma)
    else:
        ma = me.getValue(index)
    addData(ma, ufo)
    return ma

def update(map, ufo):
    city = ufo["city"]
    index = om.get(map, city)
    if index is None:
        ma = newufo()
        om.put(map, city,ma)
    else:
        ma = me.getValue(index)
    addData(ma, ufo)
    return ma
def addData(ma, ufo):
    indice = ma["indice"]
    lt.addLast(indice, ufo)
    return(ma)
def newufo():
    entry = {
        "indice" : None,
     }
    entry["indice"] = lt.newList('SINGLELINKED', comparedatetime)
    return(entry)
def newufoh():
    entry = {
        "indice" : None,
     }
    entry["indice"] = lt.newList('SINGLELINKED', comparehour)
    return(entry)

def req1 (catalgo, ciudad):
    city = om.get(catalgo["cities"], ciudad)
    number = lt.size(city["value"]["indice"])
    listaorg = sa.sort(city["value"]["indice"],comparedatetime)
    first =  lt.subList(listaorg, 1 , 3)
    last = lt.subList(listaorg, lt.size(listaorg) - 3, 3)
    return(number,first,last)

def req3 (catalogo, limi, limo):
    sub = om.keys(catalogo["hour"], limi, limo)
    su  = om.values(catalogo["hour"], limi, limo)
    tot = 0
    lst = lt.newList("ARRAY_LIST")
    for i in lt.iterator(sub):
        a = om.get(catalogo["hour"], i)
        size = lt.size(a["value"]["indice"])
        tot += size
    for h in lt.iterator(su):
        lt.addLast(lst,h["indice"]["first"]["info"])
    lstord = mk.sort(lst, comparedatetime)
    a = lt.subList(lstord, 0, 3)
    b = lt.subList(lstord, lt.size(lstord) - 3, 3)
    return(tot, a, b)
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def comparedatetime(ufo1, ufo2):
    date1 = datetime.datetime.strptime(ufo1["datetime"], '%Y-%m-%d %H:%M:%S')
    date2 = datetime.datetime.strptime(ufo2["datetime"], '%Y-%m-%d %H:%M:%S')
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
def comparehour(date1, date2):
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1