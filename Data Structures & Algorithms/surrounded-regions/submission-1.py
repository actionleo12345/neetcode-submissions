class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def convert_O_to_T(r, c):
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                board[r][c] != "O"):
                return
            
            board[r][c] = "T"
            convert_O_to_T(r-1,c)
            convert_O_to_T(r+1,c)
            convert_O_to_T(r,c-1)
            convert_O_to_T(r,c+1)

        # 1. convert all the unsurrounded O to T
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and 
                    (r in [0, rows-1] or c in [0, cols-1])):
                    convert_O_to_T(r, c)

        # 2. next, we convert all the surrounded O to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. lastly, convert the unsurrounded "T" back to "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        