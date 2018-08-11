#A vector e.g. [1, 2 ,3]  is defined as a lsit of values where 1 is the x component, 2 the y component...

from math import sqrt

def length(vector):
    return sqrt(sum([component ** 2 for component in vector]))

def unit_vector(vector):
    return div_scalar([vector], length(vector))

def zero_vector(dimension):
    return [0 for i in range(dimension)]

def concat(vectors, combine):
    combined_vector = vectors[0]

    for i in range(0, len(vectors)):
        if i > 0:
            _check_dimensions(vectors, i)
            for j in range(0, len(vectors[0])):
                combined_vector[j] = combine(combined_vector[j], vectors[i][j])

    return combined_vector

def add(vectors):
    return concat(vectors, lambda a, b: a + b)

def sub(vectors):
    return concat(vectors, lambda a, b: a - b)

def mul_scalar(vectors, scalar):
    return [scalar * component for component in add(vectors)]

def div_scalar(vectors, scalar):
    return mul_scalar(vectors, 1 / scalar)

def dot_product(vectors):
    dot = 0

    for i in range(1, len(vectors)):
        _check_dimensions(vectors, i)
        for j in range(0, len(vectors[0])):
            dot += vectors[i-1][j] * vectors[i][j]

    return dot

def _check_dimensions(vectors, i):
    if len(vectors[i-1]) != len(vectors[i]):
        raise Exception('Vectors must be the same dimensions!')


a_s = 3

a = [1,2,3]
b = [4,-5,6]
c = [1,2,3]

print(dot_product([a,b]))
