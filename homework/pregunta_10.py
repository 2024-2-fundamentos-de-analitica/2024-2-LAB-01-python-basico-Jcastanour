"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def loadinput(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file,delimiter='\t')
        for row in reader:
                letras = len(row[3].split(",") )
                diccionario = len(row[4].split(",")) 
                data.append((row[0], letras, diccionario))
    return (data)

def tuples(data):
    tuplas = []
    for row in data:
        tuplas.append((row[0], int(row[1])))
    return tuplas

def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[0])
        
def reducer(sequence):
    """Reducer"""
    result = {}
    for key, value in sequence:
        if key not in result.keys():
            result[key] = [value]
        else:
            result[key].append(value)
    return list(result.items())

def max_min(sequence):
    maximin = []
    for key, value in sequence:
        maximo = max(value)
        minimo = min(value)
        maximin.append((key,minimo, maximo))
    return maximin

def pregunta_10():

    data = loadinput("files/input/data.csv")
    # tuplas = tuples(data)

    return data

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
print(pregunta_10())