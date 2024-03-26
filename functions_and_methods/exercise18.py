def remainders_3(numbers):
    return [number % 3 for number in numbers]

dict_of_lists = {
    'numbers_1' : [0, 1, 2, 3, 4, 5, 6],
    'numbers_2' : [1, 2, 4, 5],
    'numbers_3' : [0, 3, 6],
    'numbers_4' : []
    }

for key in dict_of_lists:
    if any(remainders_3(dict_of_lists[key])) != 0:
        print(f'{key} contains at least one number that is not evenly divided by 3')
