def factorial(number):
    result = 1 
    for i in range (number, 0, -1):
        result *=number
        print(result)
        print(i)
        print(number)
    return result 

print(factorial(10))


