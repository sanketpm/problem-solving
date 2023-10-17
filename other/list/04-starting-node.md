## Links
[Leetcode](https://leetcode.com/problems/linked-list-cycle-ii/description/)

## Expected Output
Length of the Cycle in the list

## Approach
1. Slow and fast pointer to check if List has loop.
    - If `YES`: record the **intersection node**
2. Calculate the length using **intersection node**
    - Have a `temp` node traverse till it reaches intersection node.
    - Increment the counter for each node traversed
3. Slow & Fast Pointer to find **Starting Node**
    - Move fast pointer `cycle-length` times
    - Now, Move both slow & fast pointers 1 node at a time, eventually they will intersect at the starting point.

## Logic
- If a Cycle exists, slow and fast pointers will intersect
- If a Cycle exists & we have intersection node, we reach the same node again when traversed forward.
- If we move fast pointer `cycle-length` times, they will intersect at starting point

```
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {

    private ListNode getIntersectionNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if( slow == fast ) {
                return slow;
            }
        }

        return null;
    }

    private int getCycleLength(ListNode head) {
        ListNode intersectNode = getIntersectionNode(head);
        ListNode temp = intersectNode;

        if(temp == null) {
            return 0;
        }

        int count = 1;

        while(temp.next != intersectNode ) {
            ++count;
            temp = temp.next;
        }

        return count;
    }

    public ListNode detectCycle(ListNode head) {
        if(head == null || head.next == null) {
            return null;
        }

        int cycleLength = getCycleLength(head);

        if(cycleLength == 0 ) {
            return null;
        }

        ListNode slow = head;
        ListNode fast = head;
        int res = 0;

        while(cycleLength != 0) {
            fast = fast.next;
            --cycleLength;
        }

        while( slow != fast ) {
            slow = slow.next;
            fast = fast.next;
            ++res;
        }

        return slow;
    }
}
```