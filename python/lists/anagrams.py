from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            xs = s
            count = [0] * 26

            for ch in s:
                xch = ch
                count[ord(ch) - ord("a")] += 1
            
            anagrams[tuple(count)].append(s)
       
        return anagrams.values()

# res = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# print(res)

'''
use defaultDict if you - do want a `key error`, 
based on the value you pass to defaultdict(), whenever a key that doesnt exist in the map
is accessed the default value is returned
'''
smap = defaultdict(lambda: 0)
smap = defaultdict(lambda: [])
print(smap[1])