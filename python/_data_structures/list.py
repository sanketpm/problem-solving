# Declaring & Initialization
lst = []

# Add, remove, size 
lst.append(10)
lst.append(20)
lst.append(30)
lst.append(40)
lst.append(50)

print(lst)


# remove the last inserted
lst.pop()
print(lst)


# I want [1, 2, 3, 4]
lst1 = [1, 2, 3]
lst2 = [2, 3, 4]
res = lst1 + lst2[2:]
print(res)

lst3 = []
lst3(lst1)

print(lst3)