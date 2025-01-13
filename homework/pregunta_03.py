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
            result[key] = 0
        result[key] += value
    return list(result.items())

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    data = loadinput("files/input/data.csv")
    tuplas = tuples(data)
    tuplas = shuffle_and_sort(tuplas)
    tuplas = reducer(tuplas)


    return tuplas

