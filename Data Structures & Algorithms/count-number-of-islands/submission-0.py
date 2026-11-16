class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        number_islands = 0

        def dfs(r, c):
            if (r < 0 or r >= len(grid) or
                c < 0 or c >= len(grid[0]) or
                (r, c) in visited or
                grid[r][c] == '0'
            ):
                return

            visited.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in directions:
                dfs(r + dr, c + dc)


        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if(grid[r][c] == '1' and (r,c) not in visited):
                    dfs(r, c)
                    number_islands += 1
        return number_islands
                