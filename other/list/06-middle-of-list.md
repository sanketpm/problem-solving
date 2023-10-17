## Links
[Leetcode](https://leetcode.com/problems/middle-of-the-linked-list/description/)

## Expected Output
Intersection Node if Lists intersect else `null`

## Approach
1. Slow and Fast Pointer
    a. Slow -> move 1 node per iteration
    b. Fast -> move 2 nodes per iteration

## Logic
- With the above approach - we know that when fast pointer reaches the end/ ahead of end (`null`), the slow pointer will be pointing to the middle of the list

```
class Solution {
    public ListNode middleNode(ListNode head) {
        if(head == null || head.next == null) {
            return head;
        }

        ListNode slow = head;
        ListNode fast = head;

        while( fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }
}
```