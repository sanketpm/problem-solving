class Solution:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, n in enumerate(nums):
            diff = target - n

            if diff in map:
                return[map[diff], i]
            
            map[n] = i
            
        return []

result = Solution().twosum([2, 5, 11, 15], 7)
print(result)