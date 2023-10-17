## Links
[Leetcode](https://leetcode.com/problems/reverse-linked-list/description/)

## Expected Output
Reverse the List and return the head pointer

## Approach
1. Recusive solution
2. Iterative solution
3. Optimized solution

**Recursive solution**
```
class Solution {
    public ListNode reverseList(ListNode head) {
        if( head == null || head.next == null ) {
            return head;
        }

        ListNode rev = reverseList(head.next);
        head.next.next = head;
        head.next = null;

        return rev;
    }
}

```

**Stack solution**
```
class Solution {
    public ListNode reverseList(ListNode head) {
        if( head == null || head.next == null ) {
            return head;
        }

        LinkedList<ListNode> stk = new LinkedList<>();
        ListNode temp = head;
        
        while(temp.next != null) {
            stk.push(temp);
            temp = temp.next;
        }

        head = temp;

        while( !stk.isEmpty() ) {
            temp.next = stk.peek();
            stk.pop();
            temp = temp.next;
        }

        temp.next = null;

        return head;
    }
}

```

**Optimized Solution**
```
class Solution {
    public ListNode reverseList(ListNode head) {
        if( head == null || head.next == null ) {
            return head;
        }
        
        ListNode prev = null;
        ListNode curr = head;
        ListNode next = null;

        while( curr != null ) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
}
```