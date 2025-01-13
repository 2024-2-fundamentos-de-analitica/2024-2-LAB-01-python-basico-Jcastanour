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
                letras = row[3].split(",") 
                data.append((row[1],letras))  
    return data

def tuples(data):
    tuplas = []
    for key, value in data:
        for valor in value:
            tuplas.append((valor, key))
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



def pregunta_11():
    data = loadinput("files/input/data.csv")
    tupla = tuples(data)
    tupla = shuffle_and_sort(tupla)
    tupla = reducer(tupla)

    return tupla
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

print(pregunta_11())    