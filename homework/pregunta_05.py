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
        reader = csv.reader(file)
        # print(reader)
        for row in reader:
            data.append(row[0].split("\t"))  # Cada fila es una lista
    return data

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
        maximin.append((key,maximo, minimo))
    return maximin

def pregunta_05():

    data = loadinput("files/input/data.csv")
    tuplas = tuples(data)
    tuplasordenadas = shuffle_and_sort(tuplas)
    tuplas = reducer(tuplasordenadas)        
    tuplas = max_min(tuplas)
    return tuplas
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

print(pregunta_05()) 