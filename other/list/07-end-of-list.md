## Links
[GFG](https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1?)

## Expected Output
Nth node at the end of LinkedList

## Approach
1. Find the size of LinkedList
2. Find the pos of Nth element from start ( size - n )
3. Traverse till you reach that position

## Logic
```
class GfG {
    
    int getNthFromLast(Node head, int n) {
        if(head == null || head.next == null) {
            return -1;
        }
        
        int size = 1;
        Node temp = head;
        
        while( (temp = temp.next) != null ) {
            ++size;
        }
        
        if(n > size) {
            return -1;
        }
        
        size = size - n;
        temp = head;
        while(size > 0) {
            temp = temp.next;
            --size;
        }
        
        return temp.data;
    }
}
```

## Python

```
def lengthOfList(head):
    curr = head
    cnt = 0
    
    while curr:
        cnt += 1
        curr = curr.next
    
    return cnt
    
def getNthFromLast(head,n):
    pos = lengthOfList(head) - n
    curr = head
    
    while curr:
        if pos == 0:
            return curr.data
        
        pos -= 1
        curr = curr.next
    
    return -1
```