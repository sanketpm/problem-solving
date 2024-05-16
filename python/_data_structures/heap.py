'''
heapq : Heap library provided by python

- By default - Python implements `min-heap`.
- Min Heap - default implementation 
- Max Heap - multiply `-1` for each element to put into heap

**Min heap**
- smallest element is the root of the tree
- smallest element gets popped out - on each pop operation

**Max heap**
- Largest element is the root of the tree
- Largest element gets popped out - on each pop operation

'''
import heapq

# a = [5, 3, 1, 2, 4]
# heapq.heapify(a)

# for i in range(len(a)):
#     print(heapq.heappop(a), end=' ') # 1 2 3 4 5

# print()

'''
Till Now
    1. Push / Pop
    2. Heapify

can (1) & (2) be combined : YES
heappq.heappush(pq, val)
heappq.heappop(pq, val)
'''
# a = [5, 3, 1, 2, 4]
# heapq.heapify(a)
# heapq.heappush(a, 6)
# print(a)

a = [
    [0, 10],
    [2, 20],
    [5, 50],
    [4, 40],
    [3, 30],
    [1, 10]
]

# queue = []
# for l in a:
#     queue.append(l)

# heapq.heapify(queue)

# for l in a:
#     print(heapq.heappop(queue))


heapq.heapify([3, 1,  4, 5])

print(heapq.heappop())
