
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

# Leer el archivo y almacenarlo en una lista
def loadinput(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # print(reader)
        for row in reader:
            data.append(row[0].split("\t"))  # Cada fila es una lista
    return data


def calculate_sum(data):
    sum = 0
    for row in data:
        sum += int(row[1])
    return sum

def pregunta_01():

    """
    Retorne la suma de la segunda columna.
    Rta/
    214

    """

    data = loadinput("files/input/data.csv")
    print(data)
    sum = calculate_sum(data)


    return sum


print(pregunta_01())