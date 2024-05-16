from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        freq_map = defaultdict(lambda: 0)

        for num in nums:
            freq_map[num] += 1

        q = [] 

        for key in freq_map.keys():
            heapq.heappush(q, (freq_map[key], key))

            if len(q) > k:
                heapq.heappop(q)

        res = [val for freq, val in q]

        return res

# nums = [1, 1, 1, 2, 2, 3]
nums = [4,1,-1,2,-1,2,3]
print(Solution().topKFrequent(nums, 2))

