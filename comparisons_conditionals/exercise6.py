def capitalize_long_strings(string):
    if len(string) > 10:
        print(string.upper())
    else:
        print(string)


capitalize_long_strings('hello world')
capitalize_long_strings('goodbye')

# Other way to do it per LS

def caps_long(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string
    
print(caps_long("Sue Smith"))     # Sue Smith
print(caps_long("Sue Roberts"))   # SUE ROBERTS
print(caps_long("Joe Shea"))      # Joe Shea
print(caps_long("Joe Stevens"))   # JOE STEVENS