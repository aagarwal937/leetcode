# NOTE: 576. Out of Boundary Paths

# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

# Example 1:

# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
# Example 2:

# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12
 
# Constraints:
# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow < m
# 0 <= startColumn < n

# NOTE: 

# SOLUTION: PYTHON3
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for move in range(1, maxMove + 1):
            for row in range(m):
                for col in range(n):
                    dp[move][row][col] = sum(
                        dp[move - 1][row + dr][col + dc] if 0 <= row + dr < m and 0 <= col + dc < n else 1
                        for dr, dc in directions
                    ) % MOD

        return dp[maxMove][startRow][startColumn]
        # MOD = 10**9 + 7
        # dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # for move in range(1, maxMove + 1):
        #     for row in range(m):
        #         for col in range(n):
        #             for dr, dc in directions:
        #                 nr, nc = row + dr, col + dc
        #                 if nr < 0 or nr >= m or nc < 0 or nc >= n:
        #                     dp[move][row][col] += 1
        #                 else:
        #                     dp[move][row][col] += dp[move - 1][nr][nc]
        #                 dp[move][row][col] %= MOD

        # return dp[maxMove][startRow][startColumn]
        
# TIME COMPLEXITY: 