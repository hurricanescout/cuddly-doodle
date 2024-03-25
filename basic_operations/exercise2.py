number = 4936

last_digit = number % 10

digit_output = str(last_digit)

print('Ones place is '+ digit_output )

number = (number - last_digit) // 10

last_digit = number % 10

digital_output = str(last_digit) 

print('Tens place is ' + digital_output)

number = (number - last_digit) // 10

last_digit = number % 10

digital_output = str(last_digit)

print('Hundreds place is ' + digital_output)

number = (number - last_digit) // 10

digital_output = str(number)

print('Thousands place is ' + digital_output)