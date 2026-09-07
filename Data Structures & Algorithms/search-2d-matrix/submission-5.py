class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])
        
        left = 0
        right = ROWS * COLUMNS - 1
        while left <= right:
            mid = left + (right - left) // 2
            row_idx = mid // COLUMNS
            col_idx = mid % COLUMNS
            print(row_idx)
            print(col_idx)
            if target == matrix[row_idx][col_idx]:
                return True
            elif target > matrix[row_idx][col_idx]:
                left = mid + 1
            else:
                right = mid - 1
        return False


          



            