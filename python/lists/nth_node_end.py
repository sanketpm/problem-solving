class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        tail = head

        while tail:
            length += 1
            tail = tail.next
        
        diff = length - n

        for i in range(length - 1):
            tail = tail.next
        
        tail.next = tail.next.next

        return head


dummy = ListNode(0)
curr = dummy

curr.next = ListNode(1)
curr = curr.next

curr.next = ListNode(2)
curr = curr.next

curr.next = ListNode(3)
curr = curr.next

curr.next = ListNode(4)
curr = curr.next

curr.next = ListNode(5)
curr = curr.next

curr = dummy.next

while curr:
    print(curr.val, end=' ')
    curr = curr.next

res = Solution().removeNthFromEnd(dummy.next, 2)