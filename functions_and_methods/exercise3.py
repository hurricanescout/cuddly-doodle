def multiply(a, b):
    product = a * b 
    return product 

def get_number(prompt):
    entry = input(prompt)
    return float(entry) 

first_number = get_number("Enter the first number: ")
second_number = get_number("Enter the second number: ")

result = multiply(first_number, second_number)

print(f'{first_number} * {second_number} = {result}')
