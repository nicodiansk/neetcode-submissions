class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        NROWS = m
        NCOLS = n
        row = [1]*NCOLS
        
        for r in range(NROWS-1):
            newRow = [1]*NCOLS
            for c in range(NCOLS-2, -1, -1):
                newRow[c] = newRow[c+1]+row[c]
            row = newRow
        return row[0]
