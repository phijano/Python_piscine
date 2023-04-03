from vector import Vector

my_vector = Vector(6)
print(my_vector.values)
print(my_vector.shape)
my_vector.T()
print(my_vector.values)
print(my_vector.shape)
my_vector.T()
print(my_vector.values)
print(my_vector.shape)


my_vector2 = Vector((2,5))
print(my_vector2.values)
print(my_vector2.shape)
my_vector3 = Vector([[1.0], [2.0]])
print(my_vector3.values)
print(my_vector3.shape)
my_vector4 = Vector([1.0, 2.0])
print(my_vector4.values)
print(my_vector4.shape)

my_vector5 = Vector([[1.0], [2.0]])
print(my_vector5.values)
print(my_vector5.shape)
my_vector6 = Vector([[1.0], [2.0]])
print(my_vector6.values)
print(my_vector6.shape)
print(my_vector5.dot(my_vector6))

my_vector7 = Vector([1.0, 2.0])
print(my_vector7.values)
print(my_vector7.shape)
my_vector8 = Vector([1.0, 2.0])
print(my_vector8.values)
print(my_vector8.shape)
print(my_vector7.dot(my_vector8))

