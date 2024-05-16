class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        n = len(nums)

        dp = [0] * (target + 1)

        dp[target] = 1

        for tar in range(target, -1, -1):
            for i in range(n):
                if tar + nums[i] > target:
                    continue
                
                dp[tar] += dp[nums[i] + tar]
        
        return dp[0]

res = Solution().combinationSum4([1, 2, 3], 4)

print(res)