import random

highest = 10

while True:
    number = random.randrange(highest + 1)
    if number == highest:
        print(number)
        break