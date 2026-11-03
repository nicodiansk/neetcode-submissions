class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        fresh = 0
        minutes = 0

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:

            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1):
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1

