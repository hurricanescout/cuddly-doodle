info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

new_string = ''

n = len(info)

for i in range(0,n): 
    if info[i] == ':':
        new_string = new_string + '+'
    else:
        new_string = new_string + info[i]

print(new_string)
