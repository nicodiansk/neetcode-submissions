class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre]+=1
        q = deque()
        #preparo la coda
        for n in range(numCourses):
            if indegree[n] == 0:
                #nodo pronto
                q.append(n)
        canFinish = 0
        res = []
        while q:
            crs = q.popleft()
            res.append(crs)
            canFinish+=1
            for neig in adj[crs]:
                indegree[neig] -=1
                if indegree[neig] == 0:
                    q.append(neig)
        if canFinish == numCourses:
            return res[::-1]
        return []

