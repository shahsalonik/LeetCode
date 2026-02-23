class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import copy 
        board_copy = copy.deepcopy(board)

        def numLiveNeighbors(i, j) -> int:
            count = 0
            # check top
            if i - 1 >= 0 and board_copy[i - 1][j] == 1:
                count += 1
            # check bottom
            if i + 1 < len(board_copy) and board_copy[i + 1][j] == 1:
                count += 1
            # check left
            if j - 1 >= 0 and board_copy[i][j - 1] == 1:
                count += 1
            # check right
            if j + 1 < len(board_copy[0]) and board_copy[i][j + 1] == 1:
                count += 1
            # check diagonals
            if i - 1 >= 0 and j - 1 >= 0 and board_copy[i - 1][j - 1] == 1:
                count += 1
            if i - 1 >= 0 and j + 1 < len(board_copy[0]) and board_copy[i - 1][j + 1] == 1:
                count += 1
            if i + 1 < len(board_copy) and j - 1 >= 0 and board_copy[i + 1][j - 1] == 1:
                count += 1
            if i + 1 < len(board_copy) and j + 1 < len(board_copy[0]) and board_copy[i + 1][j + 1] == 1:
                count += 1
            return count

        for r in range(len(board)):
            for c in range(len(board[0])):
                cell = board_copy[r][c]
                # Any live cell with fewer than two live neighbors dies as if caused by under-population.
                if cell == 1 and numLiveNeighbors(r, c) < 2:
                    board[r][c] = 0
                # Any live cell with two or three live neighbors lives on to the next generation.
                elif cell == 1 and numLiveNeighbors(r, c) <= 3:
                    board[r][c] = 1
                # Any live cell with more than three live neighbors dies, as if by over-population.
                elif cell == 1 and numLiveNeighbors(r, c) > 3:
                    board[r][c] = 0
                # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                elif cell == 0 and numLiveNeighbors(r, c) == 3:
                    board[r][c] = 1