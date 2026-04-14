class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row check

        for i in range(len(board)):
            row_set = set()
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])

        # col check

        for i in range(len(board)):
            col_set = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in col_set:
                    return False

                col_set.add(board[j][i])

        # box grid check
        # will complete check in rows and cols pair of 3x3

        for box_row in range(3):
            for box_col in range(3):

                box_set = set()

                for i in range(3):
                    for j in range(3):
                        val = board[box_row*3+i][box_col*3+j]

                        if val == ".":
                            continue
                        if val in box_set:
                            return False
                        box_set.add(val)      


        return True                

                
        