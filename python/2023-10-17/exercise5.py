def scalar_product(scalar, vector):
    for i in range(0,len(vector)):
        vector[i] = vector[i] * scalar
    return vector

def vector_addition(vector1, vector2):
    if (len(vector1) != len(vector2)):
        print("Error - vectors aren't the same dimension")
        return None
    newVector = []
    for i in range(0,len(vector1)):
        newVector.append(vector1[i]+vector2[i])
    return newVector

print(scalar_product(4, [2,5,1]))
print(vector_addition([2,1,12],[7,9,7]))