## Links
[Leetcode](https://leetcode.com/problems/linked-list-cycle/description/)

## Expected Output
True: If cycle exist in List. Else return false;

## Approach
1. Slow and fast pointer
    - Slow: Move 1 step at a time
    - Fast: Move 2 step at a time
    - Initially both point at the head

Note: 
Last Node is connected to any of the inner nodes\

e.g.:<br/> 
`pos` = 1, last node is connected to node at position 1\
`pos` = -1 last node is connected to null

## Dry Run
- -1, [1, 2]
-  0, [1, 2]
-  2, [1, 2, 3, 4]
- -1, []

## Logic
- If a Cycle exists, then eventually slow & fast pointer will point to the same node
- If a Cycle doesn't exit, fast pointer will hit `null` check

```
public class Solution {
    public boolean hasCycle(ListNode head) {
        if( head == null || head.next == null) {
            return false;
        }

        ListNode slow = head;
        ListNode fast = head;

        while( fast != null && fast.next != null ) {
            slow = slow.next;
            fast = fast.next.next;

            if( slow == fast ) {
                return true;
            }
        }

        return false;
    }
}
```

**Python**
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
```

**Questions**
1. Why do you check `slow == fast` after assignment of jumps, why not before?
    - Initially both are pointing to the same node, irrespective of input, loop stops & return `True` for all inputs

2. What is the name of the algorithm used?
    - Maze & Hare
    - Slow & Hast pointer