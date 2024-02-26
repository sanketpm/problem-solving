## Links
[GFG](https://practice.geeksforgeeks.org/problems/find-length-of-loop/1?)

## Expected Output
Length of the Cycle in the list

## Approach
1. Slow and fast pointer to check if List has loop.
    - If `YES`: record the **intersection node**
2. Calculate the length using **intersection node**
    - Have a `temp` node traverse till it reaches intersection node.
    - Increment the counter for each node traversed

## Logic
- If a Cycle exists, slow and fast pointers will intersect
- If a Cycle exists & we have intersection node, we reach the same node again when traversed forward.

```
class Solution
{
    static int getCycleLength(Node head) {
        Node temp = head;
        int count = 1;  // count the current node
        
        // using temp.next since temp & head at begininning point to same node, below check fails & return 1
        while(temp.next != head ) {
            ++count;
            temp = temp.next;
        }
        
        return count;
    }
    
    static int hasCycle(Node head) {
        if(head == null || head.next == null ) {
            return 0;
        }
        
        Node slow = head;
        Node fast = head;
        
        while( fast != null && fast.next != null ) {
            slow = slow.next;
            fast = fast.next.next;
            
            if( slow == fast ) {
                return getCycleLength(slow);
            }
        }
        
        return 0;
    }
    
    static int countNodesinLoop(Node head)
    {
        if( head == null || head.next == null) {
            return 0;
        }
        
        return hasCycle(head);
    }
}
```

## Python

```
def getLoopLength(head):
    temp = head
    cnt = 1
    
    while temp.next != head:
        temp = temp.next
        cnt += 1
    
    return cnt

def hasCycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return getLoopLength(slow)
    
    return 0
        
def countNodesinLoop(head):
    if not head or not head.next:
        return 0
    
    return hasCycle(head)
```