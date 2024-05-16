res = [[1]]
n = 3

left = 0
right = 0

for i in range(0, n - 1):
    temp = res[i]

    lst = []
    for j in range(len(temp) + 1):
        if j == 0:
            left = 0
            right = temp[0]
        elif j == len(temp):
            left = temp[len(temp) - 1]
            right = 0
        else:
            left = temp[j - 1]
            right = temp[j]
        
        lst.append(left + right)
    res.append(lst)


print(res)

