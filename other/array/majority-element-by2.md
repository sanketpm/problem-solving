## Links
[coding_ninjas](https://www.codingninjas.com/codestudio/problems/842495)

## Expected Output
Majority element

### Dry Run samples
- [1, 1, 1, 3]
- [1, 1, 2, 2]
- [1, 2, 3, 4]

### Brute Force
**Brute Approach**
```
public class Solution {
	public static int findMajority(int[] arr, int n) {
        int cnt = 0;

        for(int i = 0; i < n; i++) {
            cnt = 0;

            for(int j = i; j < n; j++) {
                if( arr[i] == arr[j] ) {
                    ++cnt;
                }
            }

            if( cnt > n/2 ) {
                return arr[i];
            }
        }

        return -1;
	}
}
```

### Better Approach
1. Use Map to record the occurance of each cell value
2. Return the key whose value > n/2

**Better Approach**
```
public class Solution {
	public static int findMajority(int[] arr, int n) {
		Map<Integer, Integer> map = new HashMap<>();

		for(int i = 0; i < n; i++) {
			map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);
		}

		for(int key: map.keySet()) {
			if( map.get(key) > n/2 ) {
				return key;
			}
		}

		return -1;
	}
}
```

### Optimized Approach
Use `Moore's Voting Algorithm`
1. Use the Moore's voting algorithm to get the element that can possibly be the majority element
2. Traverse the array again to get the no. of occurances of the `possibly majority element`
3. If occurance > n/2 : `element` is the majority element

**Questions**
1. What does this algorithm give?
   - It gives the the element that is possibly the `majority element`
   - You need to re-traverse the array to get the count of the element given by algorithm

**Optimized approach**
```
public class Solution {
	public static int findMajority(int[] arr, int n) {
		int cnt = 0;
		int el = 0;

		for(int i = 0; i < n; i++) {
			if( cnt == 0 ) {
				el = arr[i];
				cnt = 1;
			} else if( arr[i] == el ) {
				++cnt;
			} else {
				--cnt;
			}
		}

		cnt = 0;
		for(int i = 0; i < n; i++) {
			if( arr[i] == el ) {
				++cnt;
			}
		}

		if( cnt > n/2 ) {
			return el;
		}

		return -1;
	}
}
```

## Python

### HashMap Approach
```
def findMajorityElement(arr, n):
	count = Counter(arr)

	for num in arr:
		if count[num] > n//2:
			return num
	
	return -1
```

### Moore's Voting Algorithm
```
def findMajorityElement(arr, n):
	cnt, el = 0, 0

	for num in arr:
		if cnt == 0:
			el = num
			cnt = 1
		elif num == el:
			cnt += 1
		elif num != el:
			cnt -= 1
	
	cnt = 0
	for num in arr:
		if el == num:
			cnt += 1
		
		if cnt > n//2:
			return num

	return -1
```