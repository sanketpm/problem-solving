'''
Used to hold `key:value` pairs 
'''

# Initializing
dict = {}

# adding K:V pairs
dict['a'] = 1
dict['b'] = 2
dict['c'] = 3

# Printing whole dict
print(dict)

# Checking if a key is present
print('a' in dict)
print('b' in dict)
print('c' in dict)
print('NOT_IN_DICT' in dict)

print(dict['NOT_IN_DICT'] != None)


# Acessing values using their keys
print(dict['a'], end='  ')
print(dict['b'], end='  ')
print(dict['c'], end='  \n')

# Iterating over a dict
## Getting all keys
for i in dict:
    print(i, end='__')

print()

## Getting key & value in for each iteration
for k, v in dict.items():
    print(k,":",v, end='    ')

## Getting 


# Updating values of keys

# Removing a specific key

# Getting all keys()



'''
Code Sample to improve dict understanding
'''

# 1. Frequency Counter implementation

'''
    tasks = ['a', 'a', 'a', 'b', 'b', 'c']
    map = {}

    # putting elements into map
    for i in tasks:
        map[i] = map.get(i, 0) + 1

    print(map)
'''

arr = [1, 1, 1, 2, 2, 3]
count = collections.Counter(arr)

# displays all keys
print(count.keys())

# displays all values
print(count.values())

# display all K:V 
print(count.items())