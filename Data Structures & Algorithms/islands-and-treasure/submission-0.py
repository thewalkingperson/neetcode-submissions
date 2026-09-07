class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col, count):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == -1 or grid[row][col] < count:
                return
            
            grid[row][col] = count
            
            dfs(row + 1, col, count + 1)
            dfs(row - 1, col, count + 1)
            dfs(row, col + 1, count + 1)
            dfs(row, col - 1, count + 1)

            return


        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    dfs(row + 1, col, 1)
                    dfs(row - 1, col, 1)
                    dfs(row, col + 1, 1)
                    dfs(row, col - 1, 1)

        
        