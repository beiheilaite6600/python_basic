# Three types of Number: integer, float, complex.
my_integer = 100 # Int
my_float = 100.12 # float
my_imaginary_number = complex(100, 1) # complex

# + - * /
a = my_integer + my_float
b = my_imaginary_number / my_float
c = my_integer * my_imaginary_number
print(a)
print(b)
print(c)


# define mutiple variables in one line. 
my_integer, my_float, my_imaginary_number = 1, 1.1, complex(1, 1)

print(my_integer, my_float, my_imaginary_number)