'''
Use deque() instead of list (list too can act as a queue but add & remove takes O(n) time
while deque() takes O(1) time
'''
from collections import deque


q = deque()

q.append(1)
q.append(2)
q.append(3)
q.append(4)

print(q)

# Peeking
print(q)

# Looping till q becomes empty
while q:
    print(q.popleft())