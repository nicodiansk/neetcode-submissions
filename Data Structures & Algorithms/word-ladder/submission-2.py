class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set([beginWord])
        if endWord not in wordList:
            return 0
        
        neig = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                neig[pattern].append(word)
        q = deque([beginWord])
        res=1

        # BFS, explore the queue
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                # devo trovare i vicini
                #aka mi chiedo: che pattern segue questa parola?
                for j in range(len(word)): #per ogni carattere della parola pattern
                    pattern = word[:j]+"*"+word[j+1:]
                    for nWord in neig[pattern]:
                        if nWord not in visited:
                            visited.add(nWord)
                            q.append(nWord)
            res+=1
        return 0








