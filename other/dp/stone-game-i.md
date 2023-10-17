## links
[leetcode](https://leetcode.com/problems/stone-game)

## Expected Output


## Recursive Approach

```
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        def dfs(l, r):
            if l > r:
                return 0
            
            # even no of elements : Alice's Turn
            # odd no of elements : Bob's Turn
            even = False
            if (r - l) % 2 == 0:
                even = True
            
            # Bob's Turn: left & right choice values
            left, right = 0, 0

            # Alice's turn: left & right choice values
            if even:
                left = piles[l]
                right = piles[r]
            
            return max(
                dfs(l + 1, r) + left,
                dfs(l, r - 1) + right
            )

        alice_stones = dfs(0, n - 1)
        bob_stones = sum(piles) - alice_stones

        return alice_stones > bob_stones
```

## Memoization - Top_Down

```
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            # even no of elements : Alice's Turn
            # odd no of elements : Bob's Turn
            even = False
            if (r - l) % 2 == 0:
                even = True
            
            # Bob's Turn: left & right choice values
            left, right = 0, 0

            # Alice's turn: left & right choice values
            if even:
                left = piles[l]
                right = piles[r]
            
            dp[(l, r)] = max(
                dfs(l + 1, r) + left,
                dfs(l, r - 1) + right
            )

            return dp[(l, r)]
        
        alice_stones = dfs(0, n - 1)
        bob_stones = sum(piles) - alice_stones

        return alice_stones > bob_stones
```

## Tabulation - Bottom up

```

```