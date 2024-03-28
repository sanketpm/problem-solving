## Links
[Leetcode](https://leetcode.com/problems/gas-station/description/)
[LC_Solution](https://leetcode.com/problems/gas-station/solutions/1706142/java-c-python-an-explanation-that-ever-exists-till-now/)
## Expected Output

```
gas = [7, 1, 0, 11, 4]
cost = [5, 9, 1, 2, 5]
op = 3


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
op = 2
```

### Brute Force

**Approach**

**Efficiency**:
- Time: `O(N**2)`, Where N is .
- Space: `O(N)`, Where N is

**code**:
```
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            cur_fuel = 0
            refill_cnt = 0
            j = i

            while refill_cnt < n:
                cur_fuel += gas[j % n] - cost[j % n]

                if cur_fuel < 0:
                    break
                
                refill_cnt += 1
                j += 1
            
            if refill_cnt == n and cur_fuel >= 0:
                return i

        return -1
```

### Optimized
**Approach**

**Efficiency**:
- Time: `O(N)`
- Space: `O(1)`

**code**:
```
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        cur_fuel = 0
        fuel_stop = 0

        for i in range(n):
            cur_fuel += gas[i] - cost[i]
            if cur_fuel < 0:
                cur_fuel = 0
                fuel_stop = i + 1

        return fuel_stop
```