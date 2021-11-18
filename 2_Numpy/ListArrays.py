import array

# my_list = [True, "Hello", 42.0, 420, None]
# print([type(val) for val in my_list])

my_array_range = list(range(10))
my_array = array.array("i", my_array_range)
print(my_array)
