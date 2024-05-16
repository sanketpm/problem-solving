class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)

        el1, el2 = 0, 0
        cnt1, cnt2 = 0, 0

        for i in range(n):
            if cnt1 == 0:
                el1 = nums[i]
                cnt1 = 1
            elif el1 == nums[i]:
                cnt1 += 1
            else:
                cnt1 -= 1
        
        for i in range(n):
            if cnt2 == 0 and nums[i] != el1:
                el2 = nums[i]
                cnt2 = 1
            elif el2 == nums[i]:
                cnt2 += 1
            else:
                cnt2 -= 1
        
        cnt1, cnt2 = 0, 0
        
        for i in range(n):
            if nums[i] == el1:
                cnt1 += 1
            
            if nums[i] == el2:
                cnt2 += 1
                
        if cnt1 == cnt2:
            return [el1, el2]

        if cnt1 > (n / 2):
            return [el1]
        
        return [el2]


res = Solution().majorityElement([1, 2])
# inp = [
#     [3, 2, 3],
#     [1],
#     [1, 2],
#     [1, 1, 1, 3, 3, 3, 2, 2, 1]
# ]

# for i in range(len(inp)):
#     res = Solution().majorityElement(inp[i])
#     print(res)