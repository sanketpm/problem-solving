import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def createList(self, llist):
        dummy = ListNode(0)
        curr = dummy
        
        for v in llist:
            curr.next = ListNode(v)
            curr = curr.next
        
        return dummy.next
    
    def print(self, llist):
        head = self.createList(llist)

        curr = head

        while curr:
            print(curr.val)
            curr = curr.next
        

ListNode().print([1,2,3,4,5])