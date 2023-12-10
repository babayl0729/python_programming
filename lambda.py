# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments,
# but can only have one expression.

add_values = lambda x,y: x+y
multiply_values = lambda x,y: x*y

print(add_values(10,20))
print(multiply_values(10,20))

# exercise
# Write a lambda that accepts a single number 
# and cubes it. Save it in a variable called cube.

cube = lambda x: x ** 3
print(cube(3))

