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
    ufos["hour"] = om.newMap ("BST")
    ufos["ufo"] = lt.newList("ARRAY_LIST")
    ufos["cities"] = om.newMap("BST")
    return(ufos)
def addufo(catalog, ufo):
    lt.addLast(catalog["ufo"], ufo)
    update(catalog["cities"], ufo)
    updatehour(catalog["hour"], ufo)

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