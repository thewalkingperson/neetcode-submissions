class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= columns or (r,c) in visited or grid[r][c] == 0:
                return 0
            
            count = 1
            visited.add((r,c))

            count += dfs(r-1,c)
            count += dfs(r+1,c)
            count += dfs(r,c-1)
            count += dfs(r,c+1)

            return count


        max_size = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_size = max(max_size, dfs(r,c))

        return max_size

        