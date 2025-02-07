#https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # this puts the empty values as set by default
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                # if the current square is not ".", then we continue (basically ignoring it)
                if board[r][c] != ".":
                    # if we have already seen the same value in the same row,
                    # then this means there is a repeat in that row.
                    # if we have already seen the same value in the same column
                    # then this means there is a repeat in that column.
                    # if we have already seen the same value in the same square,
                    # then this means there is a repeat in that square.
                    if (board[r][c] in rows[r] or 
                            board[r][c] in cols[c] or
                            board[r][c] in squares[(r // 3, c // 3)]):
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r // 3, c // 3)].add(board[r][c])
        return True
