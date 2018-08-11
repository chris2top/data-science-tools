#A vector e.g. [1, 2 ,3]  is defined as a lsit of values where 1 is the x component, 2 the y component...

from math import sqrt

def length(vector):
    return sqrt(sum([component ** 2 for component in vector]))

def concat(vectors, combine):
    combined_vector = vectors[0]

    for i in range(0, len(vectors)):
        if i > 0:
            if len(vectors[i-1]) != len(vectors[i]):
                raise Exception('Vectors must be the same dimensions!')

            for j in range(0, len(vectors[0])):
                combined_vector[j] = combine(combined_vector[j], vectors[i][j])

    return combined_vector

def add(vectors):
    return concat(vectors, lambda a, b: a + b)

def sub(vectors):
    return concat(vectors, lambda a, b: a - b)

def mul_scalar(vectors, scalar):
    return [scalar * component for component in add(vectors)]


a_s = 3

a = [1,1,1]
b = [2,2,2]
c = [1,2,3]

print(length(a))
print(mul_scalar([a, b], a_s))
