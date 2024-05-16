class TrieNode:
    def __init__(self) -> None:
        self.children = {} 
        self.endChar = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch] 
        
        cur.endChar = True
    
    def search(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        
        return cur.endChar
    
    def prefix(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        
        return True


trie = Trie()
trie.insert('apple')
print(trie.search('apple'))
print(trie.search('app'))
print(trie.prefix('app'))
print(trie.prefix('pple'))