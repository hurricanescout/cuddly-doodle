my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

n = len(my_list) 
i = 0

while i < n:
    j = 0 
    k = len(my_list[i])
    while j < k:
        if my_list[i][j] % 2 == 0:
            print(my_list[i][j])
        j += 1
    i += 1

# Print all of the even numbers in the following list of nested lists. 
# This time, don't use any for loops.