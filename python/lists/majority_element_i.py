class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)

        el = 0

        cnt = 0
        for i in range(n):

            if cnt == 0:
                el = nums[i]
                cnt = 1
            elif el == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        
        cnt = 0

        for i in range(n):
            if nums[i] == el:
                cnt += 1
            
        if cnt >= (n / 2):
            return el
        
        return -1

res = Solution().majorityElement([3, 3, 4])
print(res)