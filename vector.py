#A vector e.g. [1, 2 ,3]  is defined as a lsit of values where 1 is the x component, 2 the y component...

def add(a, b):
    if length(a) != length(b):
        raise Exception('Vectors must have the same dimensions!')
