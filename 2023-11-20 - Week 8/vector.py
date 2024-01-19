class Vector:
    def __init__(self, *args):
        self._vector = []
        if (len(args) > 1):
            self._vector = list(args)
        else:
            if isinstance(args[0], list):
                self._vector = args[0]

    def __str__(self):
        if (self._vector): return '<' + str(self._vector)[1:-1] + '>'
        return '<>'

    def dim(self):
        if (self._vector == []): return 0
        return len(self._vector)

    def get(self, index):
        return self._vector[index]

    def set(self, index, value):
        self._vector[index] = value

    def scalar_product(self, scalar):
        return Vector([x*scalar for x in self._vector])

    def add(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError("Can't add vector with " +
                            type(other_vector).__qualname__)
        else:
            if self.dim() != other_vector.dim():
                raise ValueError("Vectors aren't in the same dimension!")
            else:
                return Vector([sum(x) for x in 
                               zip(self._vector, other_vector._vector)])

    def equals(self, other_vector):
        if not isinstance(other_vector, Vector):
            return False
        else:
            if self.dim() != other_vector.dim():
                return False
            else:
                return self._vector == other_vector._vector
            
    def __eq__(self, other_vector):
        return self.equals(other_vector)

    def __ne__(self, other_vector):
        return not self.equals(other_vector)

    def __add__(self, other_vector):
        return self.add(other_vector)

    def __mul__(self, scalar):
        # vector1 * 3
        return scalar * self

    def __rmul__(self, scalar):
        # 3 * vector1
        return self.scalar_product(scalar)

    def __iadd__(self, other_vector):
        return self + other_vector

    def __imul__(self, scalar):
        return scalar * self

    def __getitem__(self, index):
        return self._vector[index]

    def __setitem__(self, index, value):
        self._vector[index] = value

    def __delitem__(self, index):
        del self._vector[index]




my_vector = Vector([1, 2, 3])
print(my_vector)
print(my_vector.dim())
print(my_vector.scalar_product(5))

vector1 = Vector([1, 2, 3])
vector2 = Vector([0, 1, 3])
added = vector1.add(vector2)
print(added)

vector1 = Vector([1, 2, 3])
vector2 = Vector([1, 2, 3])
print(vector1.equals(vector2))

vector3 = Vector([0, 2, 0])
print(vector3.equals(vector1))

print(vector1 == vector2)
print(3 * vector1)

vector1 += vector2
print(vector1)

vector1 *= 23
print(vector1)

vector1 = Vector(1, 2, 3, 5, 6, 1)
vector1[2] += 5
print(vector1)