from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        fresh_count = [0]


        visited = set()
        q = deque()

        def fruitRot(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or grid[r][c] == 0:
                return 
            if grid[r][c] == 1:
                fresh_count[0] -= 1
                q.append((r,c))
            visited.add((r,c))
            if fresh_count[0] == 0:
                return iteration_counter

        for r in range(ROWS):
            for c in range(COLS):
                temp = grid[r][c]
                if temp == 2:
                    q.append((r,c))
                    visited.add((r,c))
                elif temp == 1:
                    fresh_count[0] += 1
        
        if fresh_count[0] == 0:
            return 0

        iteration_counter = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
            
                fruitRot(r + 1, c)
                fruitRot(r - 1, c)
                fruitRot(r, c + 1)
                fruitRot(r, c - 1)
            iteration_counter += 1

        if fresh_count[0] != 0:
            return -1
        
        return iteration_counter - 1
        



        

        
        