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
                    data.append((row[0],int(dicc.split(":")[1])))  
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
            result[key] = int(value)
        else:
            result[key] += int(value)
    return result


def pregunta_12():

    data = loadinput("files/input/data.csv")
    tuplas = shuffle_and_sort(data)
    tuplas = reducer(tuplas)

    return tuplas
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

print(pregunta_12())