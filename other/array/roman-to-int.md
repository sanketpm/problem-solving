## Links
[Leetcode](https://leetcode.com/problems/roman-to-integer/)

## Expected Output
Convert the given Roman Number to equivalent Integer

### Approach

**code**:
```
class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        
        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0

        for i in range(n):
            if i + 1 < n and value[s[i]] < value[s[i + 1]]:
                res -= value[s[i]]
            else:
                res += value[s[i]]
        
        return res
```

### Optimized
**Approach**


**code**:
```

```