import collections
import ListNode

def mergeTwoLists(l1, l2) -> ListNode:
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
    
    if l1:
        curr.next = l1
    elif l2:
        curr.next = l2
    
    return dummy.next

lists = [ 
    ListNode().createList([1, 4, 5]),
    ListNode().createList([1, 3, 4]),
    ListNode().createList([2, 6]),
]


lists = collections.deque(lists)

while len(lists) > 1:
    l1 = lists.popleft()
    l2 = lists.popleft()

    lists.append(mergeTwoLists(l1, l2))
    


         