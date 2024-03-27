def even_or_odd(a): 
    result = a % 2
    if result == 0:
        print('even')
    else:
        print('odd')


even_or_odd(43)
even_or_odd(20)

#Could do this with less code by incorporating a%2 in the condition

def even_or_odd_LS_solution_1(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

even_or_odd_LS_solution_1(43)
even_or_odd_LS_solution_1(20)

#ternary expression would also work per LS book 

def even_or_odd_LS_solution_2(number): 
    print('even' if number % 2 == 0 else 'odd')

even_or_odd_LS_solution_2(43)
even_or_odd_LS_solution_2(30)