## Expected Output
Nth fibonacci number

## Hints
1. fib(n) = fib(n-1) + fib(n-1)
Every nth fibonacci number is sum of (n-1)th and (n-2)th element

## Approach
1. Iterative

```
class Result {

    /*
     * Complete the 'fibonacci_series' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER n as parameter.
     */

    public static int fibonacci_series(int n) {
    // Write your code here
        int curr = 1;
        int prev1 = 1;
        int prev2 = 0;
        
        if(n==0) {
            return 0;
        }
        if(n==1 || n==2) {
            return 1;
        }
        
        for(int i = 3; i<=n; ++i) {
            prev2 = prev1;
            prev1 = curr;
            curr = prev2 + prev1;
        }

        return curr;
    }
}
```