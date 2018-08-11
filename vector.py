#A vector e.g. [1, 2 ,3]  is defined as a lsit of values where 1 is the x component, 2 the y component...

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




a = [1,2,2]
b = [2,3,4]
c = [1,2,3]

print(sub([a,b,c]))
