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
                diccionario = row[4].split(",") 
                for dicc in diccionario:
                    data.append(dicc.split(":"))  
    return data

def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[0])
        
def reducer(sequence):
    """Reducer"""
    result = {}
    for key, value in sequence:
        if key not in result.keys():
            result[key] = 0
        result[key] += 1
    return result


def pregunta_09():

    data = loadinput("files/input/data.csv")
    tuplasordenadas = shuffle_and_sort(data)
    tuplas = reducer(tuplasordenadas)

    return tuplas

    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

print(pregunta_09())