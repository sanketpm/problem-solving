## Links
[LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)

## Expected Output
Single Sorted LinkedList

## Optimized 

## Dry run
```
- [[1, 2, 3], [4, 5], [6, 7, 8]]

- [[1, 2, 3], [4, 5], [6, 7, 8], [9, 10]]
```

**code 1:**
```
class Solution:
    def mergeTwoLists(self, l1: List[Optional[ListNode]], l2: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                mergedLists.append(self.mergeTwoLists(l1, l2))
            
            lists = mergedLists
        
        return lists[0]
```

**code 2:**
```
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        
        return dummy.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        lists = collections.deque(lists)
        while len(lists) > 1:
            mergedList = collections.deque()

            while lists:
                l1 = lists.popleft()
                l2 = lists.popleft() if lists else None
                mergedList.append(self.mergeTwoLists(l1, l2))
            
            lists = mergedList

        return lists[0]
```