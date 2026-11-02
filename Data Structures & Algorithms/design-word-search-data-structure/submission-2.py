class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        r = self.root
        for c in word:
            if c not in r.children:
                r.children[c] = TrieNode()
            r = r.children[c]
        r.word = True

    def search(self, word: str) -> bool:
        #backtracking
        
        def dfs(index, root):
            cur = root
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    #explore everything
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
        
