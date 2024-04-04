dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part
            # of this line

print(dict1         is dict2) #False
print(dict1['a']    is dict2['a']) #False
print(dict1['a'][0] is dict2['a'][0]) #True
print(dict1['a'][1] is dict2['a'][1]) #True
print(dict1['b']    is dict2['b']) #False
print(dict1['b'][0] is dict2['b'][0]) #True
print(dict1['b'][1] is dict2['b'][1]) #True

#They were all true except the first. My error was in not applying reasoning
# that I used to get the correct True answers to the elements of the values
# as a whole
# The nested components are all references to the original nested objects.