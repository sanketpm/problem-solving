## Links
[Leetcode](https://leetcode.com/problems/longest-repeating-character-replacement)

## Expected Output

### Optimised

**Dry Run**
```
s = 'AABABBA', k = 2
s = 'ABABBA', k = 2
```

**Approach**
- Two pointer
- At each iteration, find the `window_len`, `max_freq_char`, using them both find the `replaceable_char`,
- `replaceable_char` must be `<=` *k*
    - True: update 'result'
    - False: slide the window 1 char forward, `l += 1`, `r += 1`
- `replaceable_char` must be `<=` *k*
    - why? if replaceable chars are k in number, replace them & whole subarray you have consist of same chars, else they when replaced they will contain other chars too.
    
**Efficiency**:
- Time: `O(26 * N)`, Where `26` time required to fetch the freq of each char from the dict at each iteration
- Space: `O(1)`, Where N is

**code**:
```
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l, r = 0, 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)

            max_char_freq = max(count.values())
            win_len = r - l + 1
            replaceable_chr = win_len - max_char_freq

            if replaceable_chr <= k:
                res = max(res, win_len)
            else:
                count[s[l]] -= 1
                l += 1
            
            # update 'r' at each iteration to avoid recounting of a char when 'if' condition fails  
            r += 1
        return res
```