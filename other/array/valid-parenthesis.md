## Links
[Leetcode](https://leetcode.com/problems/valid-parentheses/description/)

## Expected Output
True or False

## Approach
Use `stack` data structure
1. Open braces - put into stack
2. Close braces - stack top must be it's complimentary opening brace else : it's an invalid parenthesis
3. At end of iteration, if the stack is not not empty then - invalid parenthesis
4. At end of iteration, if the stack is empty - valid parenthesis

**Code**
```
class Solution {
    public boolean isValid(String s) {
        LinkedList<Character> stk = new LinkedList<>();
        Map<Character, Character> compliment = new HashMap<>();

        compliment.put(')', '(');
        compliment.put('}', '{');
        compliment.put(']', '[');

        for(char brace : s.toCharArray() ) {
            if(brace == '(' || brace == '{' || brace == '[') {
                stk.push(brace);
            } else if(stk.isEmpty() || stk.pop() != compliment.get(brace) ) {
                return false;
            }
        }

        return stk.isEmpty();
    }
}
```