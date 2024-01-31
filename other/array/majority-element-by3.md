## Links
[Leetcode](https://leetcode.com/problems/majority-element-ii/)
[coding_ninjas](https://www.codingninjas.com/codestudio/problems/893027)

## Expected Output
List of elements that occur >n/3 times

### Dry Run
- [ 2, 1, 1, 3, 1, 4, 5, 6]
- [ 1, 1, 1, 2, 3, 4, 5, 6]

- [1, 1, 1, 2, 2, 2, 3, 4]

**Observations**
- Max two elements can occur >n/3 times in list of any size

### Brute Force

**code**
```
public class Solution 
{
    public static ArrayList<Integer> majorityElementII(ArrayList<Integer> arr) 
    {
        ArrayList<Integer> res = new ArrayList<>();
        int n = arr.size();
        int cnt = 0;
        int el = 0;

        for(int i = 0; i < n; i++) {
            cnt = 0;
            el = arr.get(i);
            for(int j = i; j < n; j++) {
                if( arr.get(j) == el ) {
                    ++cnt;
                }
            }

            if( cnt > n/3 && !res.contains(el)) {
                res.add(el);
            }
        }

        return res;
    }
}
```

### Optimized
1. Use Map to record the occurance count of each val
2. Check which key's value is >n/3
    - add it to res_list

**code**
```
public class Solution 
{
    public static ArrayList<Integer> majorityElementII(ArrayList<Integer> arr) 
    {
        Map<Integer, Integer> map = new HashMap<>();
        ArrayList<Integer> res = new ArrayList<>();
        
        int n = arr.size();
        int el = 0;

        for(int i = 0; i < n; i++) {
            el = arr.get(i);
            map.put(el, map.getOrDefault(el, 0) + 1);
        }

        for(int key: map.keySet()) {
            if( map.get(key) > n/3) {
                res.add(key);
            }
        }

        return res;
    }
}
```

### Optimized Approach
1. Modified - Find Majority Element n/2

> NOTE: Add an extra check at cnt1==0 and cnt2 == 0, why? to avoid the same val to be counted seperately
**code**

```
public class Solution 
{
    public static ArrayList<Integer> majorityElementII(ArrayList<Integer> arr) 
    {
        Map<Integer, Integer> map = new HashMap<>();
        ArrayList<Integer> res = new ArrayList<>();
        
        int n = arr.size();
        
        int cnt1 = 0, cnt2 = 0;
        int el1 = 0, el2 = 0;
        int val = 0;

        for(int i = 0; i < n; i++) {
            val = arr.get(i);

            if( cnt1 == 0 && val != el2 ) {
                el1 = val;
                ++cnt1;
            }
            else if( cnt2 == 0 && val != el1 ) {
                el2 = val;
                ++cnt2;
            }
            else if( val == el1 ) {
                ++cnt1;
            }
            else if( val == el2 ) {
                ++cnt2;
            }
            else {
                --cnt1;
                --cnt2;
            }
        }

        cnt1 = 0;
        cnt2 = 0;

        for(int i = 0; i < n; i++) {
            val = arr.get(i);
            
            if(val == el1) {
                ++cnt1;
            }

            if( val == el2 ) {
                ++cnt2;
            }
        }

        if( cnt1 >  n/3 ) {
            res.add(el1);
        }

        if( cnt2 > n/3 ) {
            res.add(el2);
        }

        return res;
    }
}
```