class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses #num archi entranti/pre
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[pre]+=1
            adj[crs].append(pre)
        
        #inizializzo coda con quelli senza prereqs
        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        res = []
        canFinish = numCourses #decremento
        while q:
            node = q.popleft()
            res.append(node)
            canFinish-=1
            for nei in adj[node]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if canFinish == 0:
            return res[::-1]
        return []
