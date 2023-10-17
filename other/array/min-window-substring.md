## Links
[Leetcode](https://leetcode.com/problems/minimum-window-substring/description/)

## Expected Output
Minimum Substring `s` that contains all the letters of `t`

## Approach
**Sliding Windows**
1. Have to Maps to compare the occurance of each character
   1. `sMap`: contains **char : count**
   2. `tMap`: used to match the char & count of sMap
2. Two-pointer traversing of a string ( at each character ) :
   1. If s[end] exist in sMap
      1. Increment the value-count in `tMap`
      2. If `tMap` value becomes equal to `sMap` value => `++match` counter 
   2. **While** `match == sMap.size()`
      1. Update the maxWindow length
      2. Increment the `start` pointer to reduce the window length


**Code**
```
class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        for(char x : t.toCharArray() ) {
            sMap.put(x, sMap.getOrDefault(x, 0) + 1);
        }

        int start = 0;
        int end = 0;

        int match = 0;
        
        int minWin = Integer.MAX_VALUE;
        int subStr = 0;

        while( end < s.length() ) {
            char x = s.charAt(end);

            if( sMap.containsKey(x) ) {
                tMap.put(x, tMap.getOrDefault(x, 0) + 1);

                if( sMap.get(x) == tMap.get(x) ) {
                    ++match;
                }
            }

            while( match == sMap.size() ) {
                // record current window
                int currWin = end - start + 1;

                if( currWin < minWin ) {
                    minWin = currWin;
                    subStr = start;
                }

                // decrement window length
                char del = s.charAt(start);
                ++start;

                if( sMap.containsKey(del) ) {
                    if( sMap.get(del) == tMap.get(del) ) {
                        --match;
                    }
                    tMap.put(del, tMap.get(del) - 1);
                }
            }
            ++end;
        }

        if( minWin == Integer.MAX_VALUE) {
            return "";
        }

        return s.substring(subStr, subStr+minWin);
    }
}
```

**Python**

```
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        tmap = Counter(t)
        smap = {}

        have, need = 0, len(tmap)

        minLen = float('inf')
        substr = [-1, -1]

        l, r = 0, 0

        while r < len(s):
            if s[r] in tmap:
                smap[s[r]] = 1 + smap.get(s[r], 0)

                if smap[s[r]] == tmap[s[r]]:
                    have += 1
            
            while need == have:
                winLen = r - l + 1

                if winLen < minLen:
                    minLen = winLen
                    substr = [l, r + 1]
                
                if s[l] in tmap:
                    smap[s[l]] -= 1

                    if smap[s[l]] < tmap[s[l]]:
                        have -= 1
                
                l += 1
            r += 1
        
        return s[substr[0]:substr[1]]
```

**Edge cases:**
- t = ""
- s = "", t = ""

**Questions:**
- why is `need` == `len(tmap)` & not 'len(t)'
    Because, have is increment only it match the values of a key. but a key can have >= 10 values too, in that case need cannot be 10, need should be 1, cuz when smap[key] == 10, have is incremented
