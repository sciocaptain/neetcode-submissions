class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        # Each row must have unique, create a set for each row
        # Each column must have unique, create a set for each column
        # Each grid must have unique, create a set for each grid

        # Iterate through each item in the matrix
            # We add the x coordinate to each row
            # We add the y coordinate to each col
            # We add the x,y coordinate to each row % 3, col % 3
            # Return false if the value exists in the set already
        
        #Return True Otherwise


        r_set = [set() for i in range(len(board))]
        c_set = [set() for i in range(len(board[0]))]
        g_set = [[set() for i in range(len(board) // 3)] for j in range(len(board[0]) // 3)]

        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if (val in r_set[r] or val in c_set[c] or val in g_set[r // 3][c // 3]):
                    return False
                if val != '.':
                    r_set[r].add(val)
                    c_set[c].add(val)
                    g_set[r // 3][c // 3].add(val)
        return True