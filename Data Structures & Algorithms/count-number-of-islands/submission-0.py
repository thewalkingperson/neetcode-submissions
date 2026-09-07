class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            # Base case: out of bounds or already visited or water
            if r < 0 or c < 0 or r >= rows or c >= columns or (r,c) in visited or grid[r][c] == '0':
                return
            
            visited.add((r,c))
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
            


        islands = 0
        for r in range(rows):
            for c in range(columns):
                if (r,c) not in visited and grid[r][c] == '1':
                    dfs(r,c)
                    islands += 1
        
        return islands
        
        