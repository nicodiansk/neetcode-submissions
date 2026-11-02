class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(res) != numCourses:
            return []
        return res[::-1]