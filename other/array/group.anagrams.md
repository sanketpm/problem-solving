## Links
[Leetcode](https://leetcode.com/problems/group-anagrams/description/)

## Expected Output
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

## Approach
1. Use a HashMap to store `count[]` as a key
>note: `count[]` each index => 'ascii' value of a lower alphabetic char (a-z)
2. Parse a word & create a `count[]` array
3. Let map: `key` = count[], `value` = []
    - add the str as value to corresponding count key


**Time Complexity:** 
- `O(m * n)`, m = no of strs, n = max len of str\

**Auxiliary Space:**
- `O(26 * m)`, each str in unique 

**code**:
```
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1
            
            if not tuple(count) in res:
                res[tuple(count)] = []
            
            res[tuple(count)].append(s)
        
        return res.values()
```

### Optimized
**Approach**

**Time Complexity:** 
    - `O(N)`, Where N is ..
**Auxiliary Space:** 
    - `O(N)`, due to ...

**code**:
```

```