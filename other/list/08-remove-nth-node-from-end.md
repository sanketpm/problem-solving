## Links
[Leetcode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

## Expected Output
Remove Nth node at the end of LinkedList

## Brute Force Approach
1. Find the size of LinkedList
2. Find the pos of Nth element from start ( size - n )
3. Traverse till you reach the prev position to that node
4. Point the prev node to next's next node(prev.next = prev.next.next)

## Optimized Approach
1. Use Fast & Slow pointer
2. Move the `Fast` Pointer to N nodes ahead of `slow` pointer
3. Move both `fast` & `slow` pointers one node at a time till `fast` node reaches null
4. `Slow` node now points to previous node of target node, change the `slow` pointer node to target nodes next node.

**Brute force**
```
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null || head.next == null) {
            return null;
        }

        ListNode temp = head;
        int size = 1;

        while ( (temp = temp.next) != null ) {
            ++size;
        }

        if(n > size) {
            return null;
        }

        if(size == n) {
            temp = head.next;
            head.next = null;
            head = temp;
            return temp;
        }

        size = size - n;
        temp = head;

        while(size > 1) {
            temp = temp.next;
            --size;
        }
        System.out.println(temp.val);
        temp.next = temp.next.next;
        return head;
    }
}
```

**Optimized Approach**
```
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode slow = dummy;
        ListNode fast = dummy;

        for(int i = 0; i < n; i++) {
            fast = fast.next;
        }

        while( fast.next != null ) {
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;

        return dummy.next;
    }
}
```