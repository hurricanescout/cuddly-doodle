original_tuple = (1, 2, 3, 4, 5)

temp_list = list(original_tuple[1:-1])

temp_list.sort(reverse = True)

new_tuple = tuple(temp_list)

print(new_tuple)