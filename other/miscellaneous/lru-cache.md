## Links
[Leetcode](https://leetcode.com/problems/lru-cache/)

## Expected Output
Final state of LRU Cache after series of get() & put() operations on it.

## Approach
1. We need two sepearte data structure for get() & put() thought the whole cache is is maintaned.
2. We need `map` to store `key: value` value is of type Node(custom Doubly-linked-list)
3. get(key)
   1. `key` doesnt exist in map : return -1
   2. `key` exist in map : then realign it's position in stack
      1. remove it from it's existing position
      2. insert it into head position
4. put(key, value)
   1. `key` exist in map : remove it (for realignment in cache)
   2. `map_size` == capacity? : remove the LRU-Node(least recently used) i.e., (`tail.prev`)
   3. insert the new `key: value` into the map & cache
5. both `get()` and `put()` rely on two other functions
   1. `insert()`
      1. insert the given node's key&value into the map
      2. insert the new node into the cache
   2. `remove()` 
      1. remove the key&value from the map
      2. remove the given node from it's existing position

**code**
```
class LRUCache {
    class Node {
        int key;
        int value;
        Node prev;
        Node next;

        Node(int _key, int _value) {
            key = _key;
            value = _value;
        }
    }

    private int capacity;
    Map<Integer, Node> map = new HashMap<>();
    Node head = new Node(0, 0);
    Node tail = new Node(0, 0);
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        // 1. Key doesnt exist in map return -1;
        // 2. Key exist in map
            // realign the cache-value
            //1. remove(key) : removes from it's existing position
            //2. insert(key, value): puts it into head position
            //3. return value.key (value: Node)
        if(!map.containsKey(key)) {
            return -1;
        }

        Node node = map.get(key);
        remove(node);
        insert(node);
        
        return node.value;
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)) {
            remove(map.get(key));
        }

        if(map.size() == capacity) {
            remove(tail.prev);
        }

        insert(new Node(key, value));
    }

    private void insert(Node node) {
        map.put(node.key, node);
        Node temp = head.next;
        head.next = node;
        node.prev = head;
        node.next = temp;
        temp.prev = node;
    }
    
    private void remove(Node node) {
        map.remove(node.key);
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
}
```