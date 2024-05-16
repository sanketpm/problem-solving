import heapq

tasks = ['a', 'a', 'a', 'b', 'b', 'c']
map = {}

# putting elements into map
for i in tasks:
    map[i] = map.get(i, 0) + 1

print(map)

maxHeap = []

for task, cnt in map.items():
    maxHeap.append(cnt * -1)

print(maxHeap)

heapq.heapify(maxHeap)

print(maxHeap)