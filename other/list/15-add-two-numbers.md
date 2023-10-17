## Links
[Leetcode](https://leetcode.com/problems/add-two-numbers)

## Expected Output
Sum list

## Approach
- Code is self descriptory

**Code**
```
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        int val = 0;
        int carry = 0;

        int v1 = 0, v2 = 0;

        while( l1 != null || l2 != null || carry != 0) {
            v1 = (l1 == null)? 0 : l1.val;
            v2 = (l2 == null)? 0 : l2.val;

            val = v1 + v2 + carry;

            carry = val / 10;
            val = val % 10;

            curr.next = new ListNode(val);
            curr = curr.next;

            l1 = (l1 == null)? null : l1.next;
            l2 = (l2 == null)? null : l2.next;
        }

        return dummy.next;
    }
}
```
