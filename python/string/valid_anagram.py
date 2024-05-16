import collections
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         count = [0] * 26

#         for ch in s:
#             count[ord(ch) - ord('a')] += 1
        
#         for ch in t:
#             count[ord(ch) - ord('a')] -= 1

#         for i in range(26):
#             if count[i] != 0:
#                 return False
        
#         return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = collections.defaultdict(int)
        for x in s: tracker[x] += 1
        for x in t: tracker[x] -= 1
        return all(x == 0 for x in tracker.values())

print(Solution().isAnagram('anagram', 'nagaram'))
print(Solution().isAnagram('anagram', 'nagram'))

# print(chr(97))
# print(ord('b') - ord('a'))