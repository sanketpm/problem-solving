
## Links
[Leetcode](https://leetcode.com/problems/spiral-matrix/)

## Expected Output

## Appraoch

## Questions:
1. Why did we use `if(top <= bottom)` & `if(left <= right)` inside the while loop?
   - To cover the edge when (top == bottom || left == right), we need to have a check before we execute anything without proper checking inside the while loop 

2. Why didn't you add `if` checkers for 2nd for loop?
   - Not needed cuz, thought top gets incremented and incase it becomes greater than bottom the `for` loop if condition fails & hence it will not be executed

## Dry Run example:
1. [
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10. 11, 12], 
    [13, 14, 15, 16]
   ]

2. [1, 2, 3, 4]

3. [
    [1]
    [2]
    [3]
    [4]
   ]
**Approach**
```
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        int top = 0;
        int left = 0;
        int right = matrix[0].length - 1;
        int bottom = matrix.length - 1;

        while( top <= bottom && left <= right ) {
            for(int i = left; i <= right; i++) {
                res.add( matrix[top][i] );
            }
            ++top;

            for(int i = top; i <= bottom; ++i) {
                res.add( matrix[i][right] );
            }
            --right;

            if( top <= bottom ) {
                for(int i = right; i >= left; i--) {
                    res.add( matrix[bottom][i] );
                }
                --bottom;
            }

            if( left <= right ) {
                for(int i = bottom; i >= top; i--) {
                    res.add( matrix[i][left]);
                }
                ++left;
            }
        }

        return res;
    }
}
```