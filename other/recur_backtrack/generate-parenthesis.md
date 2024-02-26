## Links
[Leetcode](https://leetcode.com/problems/generate-parentheses/)

## Expected Output

### Optimized
**Dry run:**
```
Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]
```

**code**:
```
class Solution:
    def generate(self, ob, cb, braces, res):
        if ob > cb or ob < 0:
            return

        if ob == 0 and cb == 0:
            res.append(braces)
        
        if ob <= cb:
            self.generate(ob - 1, cb, braces + '(', res)
            self.generate(ob, cb - 1, braces + ')', res)
            
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generate(n, n, '', res)

        return res
```