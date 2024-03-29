my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

my_zip = zip(my_str, my_list, my_tuple, my_range, strict = False)

print(list(my_zip))

# Final Result
# [('a', 'Alpha', None, 10),
# ('b', 'Bravo', True, 20),
# ('c', 'Charlie', False, 30)]