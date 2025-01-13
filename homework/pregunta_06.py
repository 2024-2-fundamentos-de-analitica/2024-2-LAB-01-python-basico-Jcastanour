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

def pregunta_06():

    data = loadinput("files/input/data.csv")
    tuplas = tuples(data)
    tuplasordenadas = shuffle_and_sort(tuplas)
    tuplas = reducer(tuplasordenadas)
    tuplas = max_min(tuplas)

    return tuplas

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

print(pregunta_06())