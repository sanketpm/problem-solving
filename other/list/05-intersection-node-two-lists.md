## Links
[Leetcode](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)

## Expected Output
Intersection Node if Lists intersect else `null`

## Approach
1. Brute Force
2. Better: Use Set
3. Optimized: Use the length property


**Brute Force solution**
1. For each node of list1 traverse all nodes of list2
2. If at any node they intersect then return the node
3. If the loops end => return `null`  
4. T = O(n*m), S = O(1) ( n = length of list1, m = length of list2)
```
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null) {
            return null;
        }

        ListNode temp = null;
        while( headA != null ) {
            temp = headB;
            while( temp != null ) {
                if( headA == temp ) {
                    return headA;
                }
                temp = temp.next;
            }

            headA = headA.next;
        }

        return null;
    }
}
```

**Better Solution**
1. Traverse ListA and put all nodes in set
2. Traverse ListB & at each node check if it exists in Set
    a. If `exits = true` -> return that node
    b. If traversal reach the end of the list -> return `null`
3. T = O(n+m), S = O(n)

```
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null) {
            return null;
        }

        Set<ListNode> set = new HashSet<>();
        ListNode temp = headA;

        while(temp != null) {
            set.add(temp);
            temp = temp.next;
        }

        temp = headB;

        while(temp != null) {
            if(set.contains(temp)) {
                return temp;
            }
            temp = temp.next;
        }

        return null;
    }
}
```


**Optimized Solution**
1. If `a` reaches end of listB -> point it to `headB`
2. If `b` reaches end of listA -> point it to `headA`
3. **Eventually they will point to nodes at equal length from the end**
4. They will either intersect & fail the `equality check` or they'll both reach `null` & fail the `equality check` 
5. T = O( 2 * max(n, m) ), S = O(1)
```
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null) {
            return null;
        }

        ListNode a = headA;
        ListNode b = headB;

        while( a != b ) {
            a = (a == null) ? headA: a.next;
            b = (b == null) ? headB: b.next;
        }

        return a;
    }
}
```