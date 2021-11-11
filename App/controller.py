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
 """

import config as cf
import model
import csv
def newcatalog():
    ret = model.catalog()
    return (ret)
def loaddata(catalogo):
    filename = cf.data_dir +"UFOS-utf8-small.csv"
    file = csv.DictReader(open(filename, encoding="utf-8"))
    for ufo in file:
        model.addufo(catalogo, ufo)
        model.addUfoDuracion(catalogo, ufo)
        model.addUfoFecha(catalogo,ufo)

def req1 (catalogo, city):
    return model.req1(catalogo, city)
def req3 (catalogo, keyhi, keylow):
    return model.req3(catalogo, keyhi, keylow)
def hacer_fecha(fecha):
    return model.hacer_fecha(fecha)
def req2(analyzer,lim_inf,lim_sup):
    return model.req2(analyzer,lim_inf,lim_sup)

def req4(analyzer,lim_inf,lim_sup):
    return model.req4(analyzer,lim_inf,lim_sup)
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
