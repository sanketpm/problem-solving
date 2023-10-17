## Links
[Leetcode](https://leetcode.com/problems/palindrome-linked-list/)

## Expected Output
True or False depending upon whether the List is a palindrome or not

## Brute Force Approach
1. Traverse the whole list & record in a string
2. return `str.equals(str.revers())`

## Optimized Approach
1. Go to middle position:
    a. Odd size: Go to `middle` position
    b. Even size: Go to `middle - 1` position
2. Original Approach to find Middle Position:
    a. Odd size: returns middle node
    b. Even size: return `middle+1` node
```
ORIGINAL CODE:
    while(fast != null && fast.next != null) {
        slow = slow.next;   
        fast = fast.next.next;
    }

OUR REQUIREMENT CODE:
    while( fast.next != null && fast.next.next != null ) {
        slow = slow.next;
        fast = fast.next.next;
    }
```
3. Revere all nodes that occur after middle node and update `middle.next` to point to reveresed nodes
4. Have Two pointers
    a. `fpart`: Points at `head`
    b. `spart`: Points at `middle + 1` position
5. Loop till `spart` is not null & compare their values at each node. If you mismatch is found return false, else loop ends & returns true
**Brute force**
```
class Solution {

    private ListNode reverse(ListNode head) {
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
    public boolean isPalindrome(ListNode head) {
        if(head == null || head.next == null) {
            return true;
        }

        ListNode temp = head;
        StringBuffer str = new StringBuffer("");
        while(temp != null ) {
            str.append(Integer.toString(temp.val));
            temp = temp.next;
        }

        /**
        * Always convert StringBuffer to String before making any content equality
        * comparision
        */
        return str.toString().equals(str.reverse().toString());
    }
}
```

**Optimized Approach**
```
class Solution {

    private ListNode reverse(ListNode head) {
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
    public boolean isPalindrome(ListNode head) {
        if(head == null || head.next == null) {
            return true;
        }

        ListNode slow = head;
        ListNode fast = head;

        while( fast.next != null && fast.next.next != null ) {
            slow = slow.next;
            fast = fast.next.next;
        }

        slow.next = reverse(slow.next);

        ListNode fpart = head;          //part1
        ListNode spart = slow.next;     //part2
        
        while(spart != null) {
            if( fpart.val != spart.val ) {
                return false;
            }
            fpart = fpart.next;
            spart = spart.next;
        }

        return true;
    }
}
```