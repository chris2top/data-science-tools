#A vector e.g. [1, 2 ,3]  is defined as a lsit of values where 1 is the x component, 2 the y component...

def add(vectors):
    added_vector = vectors[0]

    for i in range(0, len(vectors)):
        if i > 0:
            if len(vectors[i-1]) != len(vectors[i]):
                raise Exception('Vectors must have the same dimensions!')

            for j in range(0, len(vectors[0])):
                added_vector[j] += vectors[i][j]

    return added_vector

a = [1,2,3]
b = [2,3,4]
c = [1,2,3]

print(add([a,b,c]))
