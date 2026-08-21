class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m = len(board)
        n = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for i in range(m):
            for j in range(n):
                live = 0

                # Count live neighbors
                for di, dj in directions:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < m and 0 <= nj < n:
                        if board[ni][nj] in (1, 2):
                            live += 1

                # 1 -> live, stays live
                # 2 -> live, becomes dead
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 2

                # 0 -> dead, becomes live
                elif board[i][j] == 0:
                    if live == 3:
                        board[i][j] = 3

        # Convert temporary states to final states
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1