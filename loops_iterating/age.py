age = input('How old are you? ')
age = int(age)
print(f'You are {age} years old.')
for i in range(10, 50, 10):
    print(f'In {i} years, you will be {(age + i)} years old.')