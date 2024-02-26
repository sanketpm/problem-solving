from collections import deque

arr = [1, 3, 2, 4]
res = [-1] * len(arr)

stk = deque()

for i in range(len(arr) - 1, -1, -1):
    while stk and arr[i] > stk[-1]:
        stk.pop()
    
    if not stk:
        stk.append(-1)

    res[i] = stk[-1] 
    stk.append(arr[i])


print(res)