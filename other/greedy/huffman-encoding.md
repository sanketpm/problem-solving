## Links
[GFG](https://www.geeksforgeeks.org/problems/huffman-encoding3345/1)

## Expected Output
```
Input:
    S = "abcdef"
    f[] = {5, 9, 12, 13, 16, 45}
Output: 
    0 100 101 1100 1101 111
```

### Approach

1. Create a huffman Tree
    - using min_heap of frequencies of item(str-val, left, right)
2. DFS Traversal


**Efficiency**:
- Time:
  - min_heap creating + adding elements = `O(N)` 
  - heapingfying = `O(N)`
  - while loop: 
    - pooping two lowest freq nodes + creating a new node O(N) 
    - adding them to heap O(logN)
    - Total = O(NlogN)
  - dfs: each node is visited exactly one thence O(N):
    - O(N) + O(N) + O(N) + O(NlogN) + O(N)
    - `O(NlogN)`

- Space:
  - TreeNode : O(M) = M depends on number of characters in given string (S)
  - min_heap : O(N)
  - res      : O(N)
  - Total: O(M) + O(N) + O(N) = `O(N)`

**code**:
```
import collections
import heapq

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def dfs(self, root, res, tmp):
        if not root.left and not root.right:
            res.append(tmp)
            return
        
        self.dfs(root.left, res, tmp + '0')
        self.dfs(root.right, res, tmp + '1')
        
        return res
        
    def huffmanCodes(self,S,f,N):
        min_heap= [ TreeNode(f[i]) for i in range(N)]
        heapq.heapify(min_heap)
        
        while len(min_heap) > 1:
            left = heapq.heappop(min_heap)
            right = heapq.heappop(min_heap)
        
            new_node = TreeNode(left.val + right.val)
            new_node.left = left
            new_node.right = right
        
            heapq.heappush(min_heap, new_node)
        
        root = min_heap[0]
        res = self.dfs(root, [], '')
        return res
```