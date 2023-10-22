## Links
[Leetcode](https://leetcode.com/problems/implement-trie-prefix-tree/)

## Expected Output
Implement the Trie class:

- `Trie()`
    - Tree Data structure shape
- `void insert(String word)` 
    - Inserts the string word into the trie.
- `boolean search(String word)` 
    - Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- `boolean startsWith(String prefix)` 
    - Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise

**Explanation**
```
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True
```

### Approach

**Complexity:**
|Operation |Time Complexity | Space Complexity|
|----------|----------------|-----------------|
| Insert   | O(n)           | O(n)            |
| Search   | O(n)           | O(1)            |

**code**:
```
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True
```