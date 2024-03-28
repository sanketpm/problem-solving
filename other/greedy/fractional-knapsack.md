## Links
[GFG](https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1)

## Expected Output

```
N = 3, W = 50
value[] = {60,100,120}
weight[] = {10,20,30}

items = [ [6, 60, 10], [5, 100, 20], [4, 120, 30] ]
    50 - 10 = 40 - item1
    40 - 20 = 20 - item2
    20 - 20 = 0 - item3
    
           (10)  (20)    (20)
max_value = 60 + 100 + (20 * 4) = 240

op: 240
```

### Approach
1. Create an items list [ {'per_unit_val': ##, 'val': ##, 'wt': ## }, {...}, {...}, ...]
2. Sort the items with key = 'per_unit'
3. Fractionally / Fully select the weights bases on current W value:
   1. If `items[i]['wt'] <= W:`: calculate the value by selecting the wt fully : `max_value += items[i]['val]`, `W = W - items[i]['wt']` (W reduces)
   2. If `items[i]['wt] > W`: calculcate the value by selecting the wt partially(using per_unit_val): `max_value += W * items[i]['per_unit_val]`, `W = 0` (Knapsack is completely filled)

**Efficiency**:
- Time: `O(Nlogn)`, Where N is .
- Space: `O(N)`, Where N is

**code**:
```
class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:
    def fractionalknapsack(self, W,arr,n):
        items = []

        for i in range(n):
            items.append({
                'per_unit_val': arr[i].value/arr[i].weight, 
                'val': arr[i].value,
                'wt': arr[i].weight
            })
        
        items.sort(key=lambda x : x['per_unit_val'], reverse=True)
        
        max_value = 0
        
        for i in range(n):
            if items[i]['wt'] <= W:
                max_value += items[i]['val']
                W = W - items[i]['wt']
            else:
                max_value += W * items[i]['per_unit_val']
                W = 0
        
        return max_value
```