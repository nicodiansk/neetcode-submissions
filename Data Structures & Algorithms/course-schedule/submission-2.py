class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        indegree = [0]*numCourses

        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre]+=1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        canFinish = 0
        while q:
            crs = q.popleft()
            canFinish+=1
            for nei in adj[crs]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        

        if canFinish == numCourses:
            return True
        return False

        