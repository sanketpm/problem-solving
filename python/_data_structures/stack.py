'''
`list` can be used to realise stack operations but it has major shortcoming.
1. time complexity of push & pop operation isn't O(1)
2. Inherently `list` was meant was list ops not for stack.

therefore use: `deque`
deque class from collections module was meant for stack & queue.

use:
1. .append() -> push element into stack. O(1)
2. pop() -> pop element from the stack. O(1)

Other operations:
1. peek()   - stk[-1]
2. size()   - len(stk)
3. clear()  - stk.clear()

----
stk = deque()

# variant 1:
if stk:
    print(' stk not empty ')
else:
    print ('stk is empty)

# variant 2:
if not stk:
    print('stk is empty')



'''
from collections import deque

# declaration
stk = deque()

stk.append(10)
stk.append(20)
stk.append(30)

print(stk)

print(stk.pop())
'''

# push
stk.append(10)
stk.append(20)
stk.append(30)

print(stk)


# pop
stk.pop()
print(stk)

stk.pop()
print(stk)

stk.pop()
print(stk)
'''


# stk.append(10)
# stk.append(20)
# stk.append(30)

'''
Check is stk is empty
stk1 = deque()

if not stk:
    print('stk1 = empty')

stk2 = deque()
stk2.append(10)

if stk2:
    print('stk2 is NOT empty')

'''