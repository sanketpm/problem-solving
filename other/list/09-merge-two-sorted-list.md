## Links
[LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)

## Expected Output
Single Sorted LinkedList

## Brute Force Approach

## Optimized Approach
1. Create dummy node & have `tail` pointer to it
2. Compare L1 & L2, point `tail` node to the node with lower value & move that specific node to next & tail to next

## Dry run
- [1, 3, 5], [2, 4, 6]
- [1, 3, 5], [2]
- [1], [2, 4, 5]
- [1], []
- [], [1]
- [], []
- [1, 2, 3], []
- [], [1, 2, 4]


**Optimized Approach**
```
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        while( l1 != null && l2 != null ) {
            if( l1.val < l2.val ) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }

        // Edge Case
        if( l1 == null ) {
            tail.next = l2;
        } else {
            tail.next = l1;
        }

        return dummy.next;
    }
}
```

**Python**
```
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next
```

**Python**
Brute Force:
1. Pass each list into `mergeTwoLists` (return sorted mergedList)

```
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next 


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = None

        for lst in lists:
            curr = self.mergeTwoLists(curr, lst)

        return curr
```