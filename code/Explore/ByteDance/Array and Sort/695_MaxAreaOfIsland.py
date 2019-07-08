from typing import List


class Solution:
    # 函数里包函数
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) # 高度, 长度

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j-1) + dfs(i, j+1) # 1 + 上下左右
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0


    # dfs函数与maxAreaOfIsland函数分开
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        areas = [self.dfs(i, j) for i in range(self.m) for j in range(self.n) if grid[i][j]]
        return max(areas) if areas else 0

    def dfs(self, i, j):
        if 0 <= i < self.m and 0 <= j < self.n and self.grid[i][j]:
            self.grid[i][j] = 0
            # 1 + 上下左右
            return 1 + self.dfs(i + 1, j) + self.dfs(i - 1, j) + self.dfs(i, j - 1) + self.dfs(i, j + 1)
        return 0