class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0]*numCourses

        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre]+=1
        
        q=deque()
        canFinish = 0
        res= []

        for crs in range(numCourses):
            if indegree[crs]==0:
                q.append(crs)

        while q:
            node = q.popleft()
            canFinish+=1
            res.append(node)

            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        if canFinish!=numCourses:
            return []
        return res[::-1]

