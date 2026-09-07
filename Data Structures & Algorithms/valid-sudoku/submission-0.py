class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check each row
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    if board[i][j] in row_set:
                        return False
                    else:
                        row_set.add(board[i][j])
        
        #check each column
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                else:
                    if board[j][i] in row_set:
                        return False
                    else:
                        row_set.add(board[j][i])
        
        starting_point = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        
        #check each box
        for i in starting_point:
            box_set = set()
            for j in range(i[0],i[0] + 3):
                for k in range(i[1],i[1] + 3):
                    if board[j][k] == '.':
                        continue
                    else:
                        if board[j][k] in box_set:
                            return False
                        else:
                            box_set.add(board[j][k])

        return True

        