class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        left = [1] * length
        right = [1] * length

        prod = 1
        for i in range(length):
            prod *= nums[i]
            left[i] = prod
        
        prod = 1
        for i in range(length - 1, -1, -1):
            prod *= nums[i]
            right[i] = prod

        res = [1] * length

        res[0] = right[1]
        res[length - 1] = left[length - 2]

        for i in range(1, length - 1):
            res[i] = left[i - 1] * right[i + 1]
        
        return res

result = Solution().productExceptSelf([1,2,3,4])