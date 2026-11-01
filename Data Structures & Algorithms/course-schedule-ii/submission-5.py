class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        adj = [[] for i in range(numCourses)]
        degree = [0]*numCourses

        for crs, pre in prerequisites:
            adj[crs].append(pre)
            degree[pre]+=1
        
        canFinish = 0
        q = deque()
        for crs in range(numCourses):
            if degree[crs] == 0:
                q.append(crs)

        while q:
            node = q.popleft()
            res.append(node)
            canFinish+=1
            for pre in adj[node]:
               degree[pre]-=1
               if degree[pre] == 0:
                    q.append(pre)
        
        if canFinish == numCourses:
            return res[::-1]
        return []