# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
        
#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i -1]:
#                 return True
        
#         return False



# result = Solution().containsDuplicate([1, 2, 3, 1])
# print(result)

set = set()
set.add(10);
set.add(10);
print(set);