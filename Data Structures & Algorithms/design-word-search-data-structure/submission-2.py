class TrieNode:
    def __init__(self):
        self.children = {}   # char -> TrieNode
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.map = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.map
        for w in word: 
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_end = True
        return 

    def search(self, word: str) -> bool:

        def dfs(n, w):
            if w == '':
                return n.is_end
            
            if w[0] == ".":
                for char in n.children:
                    if dfs(n.children[char], w[1:]):
                        return True
                return False
            elif w[0] in n.children:
                return dfs(n.children[w[0]], w[1:])
            else:
                return False
        
        return dfs(self.map, word)
            




