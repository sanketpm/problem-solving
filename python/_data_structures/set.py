'''
    # Create an empty set
    my_set = set()

    # Add elements to the set
    my_set.add(1)
    my_set.add(2)
    my_set.add(3)

    print(my_set)  # Output: {1, 2, 3}

    # checking if an element exists in the set
    print( (1 in my_set) )
'''

'''
    # clear all elements in list & add new elements
    my_set.clear()

    print(my_set)

    my_set.add(10)
    my_set.add(20)
    print(my_set)
'''

# Set cannot hold list, it can hold only tuples
# 1. add tuples to set
# 2. convert tuples to list 
# 3. create a list of list(tuples are converted to list)


lst = [3, 2, 1]
lst.sort()

print(tuple(lst))

# Iterate over a set
myset = set()
myset.add(10)
myset.add(20)
myset.add(30)

for e in myset:
    print(e)
