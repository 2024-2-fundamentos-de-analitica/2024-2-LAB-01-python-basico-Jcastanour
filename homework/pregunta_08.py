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
        tuplas.append((int(row[1]),row[0]))
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
    return result

def ordenar(lista):
    tuplas = []
    for key in lista:
        tuplas.append((key, sorted(set(tuple(lista[key])))))
    return tuplas

def pregunta_08():

    data = loadinput("files/input/data.csv")
    tuplas = tuples(data)
    tuplasordenadas = shuffle_and_sort(tuplas)
    tuplas = reducer(tuplasordenadas)
    tuplas = ordenar(tuplas)

    return tuplas
    
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

print(pregunta_08())