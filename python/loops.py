list = [1, 2, 3, 4]

# for n in list:
#     print(n, end=' ')
# print()

# enumerate
# for i, val in enumerate(list):
#     print(i,':', val, end='| ')

# Print in reverse order
# for i in range(len(list) - 1, -1, -1):
#     print(list[i], end=' ')

# for i in reversed(range(len(list))):
#     print(list[i], end=' ')



# Looping from i to n
'''
range(5)       => [0, 1, 2, 3, 4] => (i = 0 ; i < 5; i++)
range(1, 5)    => [1, 2, 3, 4]    => (i = 1 ; i < 5; i++)
range(0, 1)    => [0]             => (i = 0; i < 1; i++)

range(1, 5, 1) => [1, 2, 3, 4]    => (i = 1; i < 5; i+=1)
range(1, 10, 2) => [1, 3, 5, 7, 9] => (i = 1; i < 10; i+=2)

range(5, 0, -1) => [5, 4, 3, 2, 1] => (i = 5; i > 0; i-=1)

'''
# for i in range(5, 0, -1):
#     print(i)

# Enumerate
lst = [100, 200, 300, 400]

for idx, val in enumerate(lst):
    print(idx, val)