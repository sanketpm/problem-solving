## Links
[Leetcode](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

## Expected Output

### Brute Force

**code**:
```
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endChar = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            
            cur = cur.children[ch]
        
        cur.endChar = True

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(i, root):
            cur = root

            for j in range(i, n):
                ch = word[j]

                if ch == '.':
                    for child in cur.children.values():
                        if dfs(j + 1, child):
                            return True
                            
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    
                    cur = cur.children[ch]
            
            return cur.endChar
        
        return dfs(0, self.root)
```