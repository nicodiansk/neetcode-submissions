class Node():
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = Node()
            current = current.children[c]
        current.is_word = True

    def search(self, word: str) -> bool:
        def dfs(index, root):
            current = root

            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for child in current.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in current.children:
                        return False
                    current = current.children[c]
            return current.is_word

        return dfs(0, self.root)
        
