import heapq

'''
mat

(-ones, -i)
    heap:
        [(-2, -3), (-2, 0), (-1, -2)]
    sorted:
        [(-1, -2), (-2, 0), (-2, -3)]

(-ones, i)
    heap:
        [(-2, 0), (-2, 3), (-1, 2)]
    sorted:
        [(-1, 2), (-2, 3), (-2, 0)]

'''

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        heap = []

        for i, row in enumerate(mat):
            ones = row.count(1)

            heapq.heappush(heap, (-ones, i))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        print(heap)
        heap.sort(key = lambda x: (-x[0], x[1]))
        print(heap)
        
        for _, i in heap:
            res.append(i)
        
        return res

mat = [
 [1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]
]

edge_mat = [[1,1,1,0,0,0,0],
            [1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0],
            [1,1,1,0,0,0,0],
            [1,1,1,1,1,1,1]
            ]

k = 3

res = Solution().kWeakestRows(mat, k)
print(res)