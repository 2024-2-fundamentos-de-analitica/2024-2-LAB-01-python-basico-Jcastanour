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
            data.append(row[0].split("\t")[0])  # Cada fila es una lista
    return data

def registros_letras(data):
    letras = {}
    for row in data:
        if row[0] in letras:
            letras[row[0]] += 1
        else:
            letras[row[0]] = 1
    return sorted(letras.items())

def pregunta_02():

    
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    data = loadinput("files/input/data.csv")
    letras = registros_letras(data)
    return letras




    
